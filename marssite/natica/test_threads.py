# Does NOT USE standard django client!!
# This uses an existing running server (on localhost) with assocatiated DB.
#
# EXAMPLES:
# ./manage.py test --keepdb natica.test_threads

import unittest
import requests
import subprocess
import time
#import os.path
from pathlib import Path

from marssite.settings import BASE_DIR

def tic():
    tic.start = time.perf_counter()
def toc():
    elapsed_seconds = time.perf_counter() - tic.start
    return elapsed_seconds # fractional
    

class TestIngestFromDome(unittest.TestCase):
    maxDiff = None # too see full values in DIFF on assert failure

    @classmethod
    def setUpClass(cls):
        cls.urlroot = 'http://localhost:8000/'
        cls.DROPCACHE = Path('~/.tada/dropcache').expanduser()
        cls.DROPCACHE.mkdir(parents=True, exist_ok=True)
        cls.RSYNCPWD = Path('~/.tada/rsync.pwd').expanduser()
    
    def wait_for_ingest(self, md5, timeout=None):
        """Wait until (success != None) or Timeout"""
        tic()
        while toc() < timeout:
            r = requests.post(self.urlroot+'audit/get/{}/'.format(md5))
            if r.json().get('success') != None:
                return r.json()
        return None

    def test_auditinit_ok(self):
        """Initial audit record, as Dome might initiate"""
        url = self.urlroot + 'audit/initial/'
        params = dict(overwrite =  True,
                      md5sum =  "c89350d2f507a883bc6a3e9a6f418a10",
                      obsday = "2016-05-12",
                      telescope = "kp09m",
                      instrument = "whirc",
                      srcpath =  "/data/whirc/20165012/foo1.fits")
        r = requests.post(url, json=params)
        r = requests.post(url, json=params)
        #print('DBG test_auditinit: response={}'.format(r.content.decode()))
        expected='SUCCESS: added audit record: c89350d2f507a883bc6a3e9a6f418a10'
        self.assertEqual(expected,r.content.decode())

    def test_auditinit_dupe(self):
        """Initial audit record, as Dome might initiate"""
        url = self.urlroot + 'audit/initial/'
        params = dict(overwrite =  False,
                      md5sum =  "c89350d2f507a883bc6a3e9a6f418a10",
                      obsday = "2016-05-12",
                      telescope = "kp09m",
                      instrument = "whirc",
                      srcpath =  "/data/whirc/20165012/foo1.fits")
        r = requests.post(url, json=params)
        r = requests.post(url, json=params)
        #print('DBG test_auditinit_dupe: response={}'.format(r.content.decode()))
        expected='''FAILED to add audit record: c89350d2f507a883bc6a3e9a6f418a10; duplicate key value violates unique constraint "audit_auditrecord_pkey"
DETAIL:  Key (md5sum)=(c89350d2f507a883bc6a3e9a6f418a10) already exists.
'''
        self.assertEqual(expected,r.content.decode())

    # Thread for Successful ingest:
    # 1. post initial audit record from mock DOME
    #    - audit record available in admin/audit/auditrecord
    # 2. rsync file to mtn dropbox from mock DOME
    # 3. mtn: compress, update audit, rsync to valley DATAQ
    #    - audit record updated in admin/audit/auditrecord
    # 4. valley: pop DATAQ, ingest via NATICA webservice
    #    - audit record updated in admin/audit/auditrecord
    # 5. do natica/search (mock portal) to find ingested file
    #    - audit record updated in admin/audit/auditrecord (success=True)
    #    - no Errors or Warnings in logs on Mtn, Valley, or Natica
    def test_thread(self):
        """Full successful ingest thread for FITS. (Dome,Mtn,Val,Natica)"""
        # date/tele_inst = 20141220/wiyn-whirc
        fits = Path(BASE_DIR, 'test-data/obj_355.fits.fz')
        md5 = "c89350d2f507a883bc6a3e9a6f418a10"
        
        # 1. post initial audit record
        params = dict(overwrite =  True,
                      md5sum =  md5,
                      obsday = "2016-05-12",
                      telescope = "kp09m",
                      instrument = "whirc",
                      srcpath =  "/data/whirc/20165012/foo1.fits")
        r = requests.post(self.urlroot+'audit/initial/', json=params)
        #print('DBG-1 test_thread: response={}'.format(r.content.decode()))    

        # 2. rsync to dropbox
        cmd = ['rsync', '-az', '--password-file', RSYNCPWD ,
               str(DROPCACHE)+'/', 'tada@$boxhost::dropbox']
        #! subprocess.check_output(cmd) @@@

        # 4. Wait for audit record from NATICA to appear (or timeout)
        objdict = self.wait_for_ingest(md5, timeout=2) #success != NONE
        print('DBG-4 test_thread: objdict={}'.format(objdict))
        self.assertIsNotNone(objdict)
        self.assertTrue(objdict.get('success',None))

        # 5. Search
        params = {"coordinates": { "ra": 323, "dec": -1 },
                  "search_box_min": 2.0,
                  "pi": "Vivas",
                  "prop_id": "2017B-0951",
                  "obs_date": ["2017-08-10", "2017-08-20", "[]"],
                  "original_filename": 
                  "/data/small-json-scrape/c4d_170815_054546_ori.fits.json",
                  "telescope_instrument": [["ct4m","decam"],["foobar", "bar"]],
                  "exposure_time": 10,	
                  "release_date": "2017-09-14" }
        r = requests.post(self.urlroot+'natica/search/',json=params)
        print('DBG-5 test_thread: response={}'.format(r.content.decode()))            
        
if __name__ == '__main__':
    unittest.main()
    
