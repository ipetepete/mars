# Example (in mars::mars/marssite)
# ./manage.py test dal.tests
# ./manage.py test --keepdb dal.tests
# TO ADD:
#  - verify EXISTANCE of "meta" fields: dal_version, timestamp, comment, sql
#         'page_result_count', 'to_here_count', 'total_count'


from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
import dal.views
from marssite import settings
import json
from unittest import SkipTest
from . import expected as exp



class SearchTest(TestCase):
    maxDiff = None # too see full values in DIFF on assert failure
    fixtures = [#'natica-base-tables.json', 
                'search_hits.FitsFile.yaml',
                'search_hits.Proposal.yaml'
                ]


    def test_search_0(self):
        "No filter. Verify: API version."
        req = '{}'
       #!print('DBG: Using archive database: {}'.format(settings.DATABASES['archive']['HOST']))
        
        response = self.client.post('/dal/search/',
                                    content_type='application/json',
                                    data=req  )

        #print('DBG search_0: response={}'.format(response.json()))
        meta = {"dal_version": "1.0.0",
                "timestamp": "2017-07-05T11:44:05.946",
                "comment": "WARNING: Has not been tested much. Does not use IMAGE_FILTER.",
                "page_result_count": 100,
                "to_here_count": 100,
                "total_count": 11583954}
        #print('DBG: response={}'.format(response.json()))
        self.assertIn('meta', response.json())
        self.assertIn('timestamp', response.json()['meta'])
        self.assertIn('comment', response.json()['meta'])
        self.assertIn('page_result_count', response.json()['meta'])
        self.assertIn('to_here_count', response.json()['meta'])
        self.assertIn('total_count', response.json()['meta'])
        self.assertIsInstance(response.json()['meta']['page_result_count'], int)
        self.assertIsInstance(response.json()['meta']['to_here_count'], int)
        self.assertIsInstance(response.json()['meta']['total_count'], int)
        self.assertTrue(response.json()['meta']['page_result_count']
                        <= response.json()['meta']['to_here_count']
                        <= response.json()['meta']['total_count'])
        self.assertEqual(json.dumps(response.json()['meta']['dal_version']),
                         '"1.0.0"',
                         msg='Unexpected API version')
        self.assertEqual(response.status_code, 200)
        
    def test_search_1(self):
        "MVP-1. Basics."
        req = '''{
        "coordinates": { "ra": 323, "dec": -1 },
        "search_box_min": 2.0,
        "pi": "Vivas",
        "prop_id": "2017B-0951",
        "obs_date": ["2017-08-10", "2017-08-20", "[]"],
        "original_filename": 
        "/data/small-json-scrape/c4d_170815_054546_ori.fits.json",
        "telescope_instrument": [["ct4m","decam"],["foobar", "bar"]],
        "exposure_time": 10,	
        "release_date": "2017-09-14"
        }'''
#@@@    "image_filter":["raw", "calibrated"],
        response = self.client.post('/dal/search/',
                                    content_type='application/json',
                                    data=req  )
        #print('DBG search_1: response={}'.format(response.json()))
        self.assertJSONEqual(json.dumps(response.json()['resultset']),
                             json.dumps(json.loads(exp.search_1)['resultset']),
                             msg='Unexpected resultset')
        self.assertEqual(response.status_code, 200)

    # Allow extra fields for NATICA. Embed TBD list in schema later.
    @SkipTest
    def test_search_error_1(self):
        "Error in request content: extra fields sent"
        req = '''{
        "coordinates": { 
            "ra": 181.368791666667,
            "dec": -45.5396111111111
        },
        "TRY_FILENAME": "foo.fits",
        "image_filter":["raw", "calibrated"]
        }'''
        response = self.client.post('/dal/search/',
                                    content_type='application/json',
                                    data=req  )
        expected = {"errorMessage": "Extra fields ({'TRY_FILENAME'}) in search"}
        #!print('DBG0-tse-1: response={}'.format(response.content.decode()))
        self.assertJSONEqual(json.dumps(response.json()), json.dumps(expected))
        self.assertEqual(response.status_code, 400)


    def test_search_error_2(self):
        "Error in request content: non-decimal RA"
        req = '''{
        "coordinates": { 
            "ra": "somethingbad",
            "dec": -45.5396111111111
        },
        "image_filter":["raw", "calibrated"]
        }'''
        response = self.client.post('/dal/search/',
                                    content_type='application/json',
                                    data=req  )
        expected = {'errorMessage':
                    "Unexpected Error!: Can't convert 'float' object to str implicitly"}
        #self.assertJSONEqual(json.dumps(response.json()), json.dumps(expected))
        self.assertIn('JSON did not validate against /etc/mars/search-schema.json',
                      json.dumps(response.json()['errorMessage']))
        self.assertEqual(response.status_code, 400)
        
    def test_search_error_3(self):
        "Error in request content: obs_date is numeric (not valid per schema)"
        req = '{ "obs_date": 99  }'
        response = self.client.post('/dal/search/',
                                    content_type='application/json',
                                    data=req  )
        expected = {"errorMessage": "foo"}
        expected = {'errorMessage':
                    "JSON did not validate against /etc/mars/search-schema.json; "
                    "99 is not valid under any of the given schemas\n"
                    "\n"
                    "Failed validating 'anyOf' in "
                    "schema['properties']['search']['properties']['obs_date']:\n"
                    "    {'anyOf': [{'$ref': '#/definitions/date'}]}\n"
                    "\n"
                    "On instance['search']['obs_date']:\n"
                    "    99"}
        #self.assertJSONEqual(json.dumps(response.json()), json.dumps(expected))
        self.assertIn('JSON did not validate against /etc/mars/search-schema.json',
                      json.dumps(response.json()['errorMessage']))
        self.assertEqual(response.status_code, 400)
        
    def test_tipairs_0(self):
        "Return telescope/instrument pairs."
        #print('DBG: Using archive database: {}'.format(settings.DATABASES['archive']['HOST']))
        response = self.client.get('/dal/ti-pairs/')
        #print('DBG tipairs_0: response={}'.format(response.json()))
        #!print('DBG: expected={}'.format(exp.tipairs_0))
        self.assertJSONEqual(json.dumps(response.json()),
                             json.dumps(exp.tipairs_0))
        self.assertEqual(response.status_code, 200)        
        
