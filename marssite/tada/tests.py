# MOVED TO NATICA


#!from django.test import TestCase, Client, RequestFactory
#!from django.core.urlresolvers import reverse
#!from . import expected as exp
#!
#!class TadaTest(TestCase):
#!    fixtures = ['dump.tada.yaml', 'natica.yaml']
#!
#!    def setUp(self):
#!        #self.factory = RequestFactory()
#!        self.client = Client()
#!
#!    def test_table_prefix(self):
#!        response = self.client.get('/tada/prefix/')
#!        self.assertEqual(200, response.status_code)
#!        #print('DBG: response={}'.format(response.content.decode()))
#!        self.assertJSONEqual(response.content.decode(), exp.prefix)
#!
#!    def test_table_obstype(self):
#!        response = self.client.get('/tada/obs/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.obstype)
#!
#!    def test_table_proctype(self):
#!        response = self.client.get('/tada/proc/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.proctype)
#!
#!    def test_table_prodtype(self):
#!        response = self.client.get('/tada/prod/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.prodtype)
#!
#!    ########
#!    
#!    def test_table_rawreq(self):
#!        response = self.client.get('/tada/rawreq/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.rawreq)
#!
#!    def test_table_filenamereq(self):
#!        response = self.client.get('/tada/fnreq/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.filenamereq)
#!
#!    def test_table_ingestreq(self):
#!        response = self.client.get('/tada/ingestreq/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.ingestreq)
#!
#!    def test_table_ingestrec(self):
#!        response = self.client.get('/tada/ingestrec/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.ingestrec)
#!
#!    def test_table_supportreq(self):
#!        response = self.client.get('/tada/supportreq/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.supportreq)
#!
#!    def test_table_floatreq(self):
#!        response = self.client.get('/tada/floatreq/')
#!        self.assertEqual(200, response.status_code)
#!        self.assertJSONEqual(response.content.decode(), exp.floatreq)
#!        
#!
#!
#!
#!
#!        
