# ./manage.py test --keepdb natica.test_threads

import unittest
import requests

class TestIngestFromDome(unittest.TestCase):
    def test_auditinit(self):
        """Initial audit record, as Dome might initiate"""
        url = 'http://localhost:8000/audit/source/'
        jsonpayload = { "overwrite": true,
                        "observations": [
            {
                "md5sum": "c89350d2f507a883bc6a3e9a6f418a10",
                "obsday": "2016-05-12",
                "telescope": "kp09m",
                "instrument": "whirc",
                "srcpath": "/data/whirc/20165012/foo1.fits"
            },
            {
                "md5sum": "c89350d2f507a883bc6a3e9a6f418a11",
                "obsday": "2016-05-12",
                "telescope": "kp09m",
                "instrument": "whirc",
                "srcpath": "/data/whirc/20165012/foo2.fits"
            }
        ] }
        r = requests.post(url, json=jsonpayload)
        print('DBG test_auditinit: response={}'.format(r.content.decode()))
        expected='SUCCESS: added 2 records'
        self.assertEqual(expected,r.content.decode())

if __name__ == '__main__':
    unittest.main()
    
