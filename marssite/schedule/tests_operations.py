from django.urls import reverse
from django.test import TestCase, Client, RequestFactory

from .models import Slot
import schedule.views

class ScheduleTest(TestCase):
    pass

#!    # Load (special test) DB with data
#!    fixtures = ['schedule.yaml']
#!
#!    def setUp(self):
#!        self.client = Client()
#!
#!    def test_setpropid1(self):
#!        "Attempt to override existing entry"
#!        tele = 'kp4m'
#!        instrum = 'kosmos'
#!        date = '2016-02-01'
#!        propid = 'Mine'
#!        response = self.client.get('/schedule/setpropid/{}/{}/{}/{}/'
#!                                   .format(tele, instrum, date, propid))
#!        expected = '''
#!ERROR
#!COULD NOT ADD: (kp4m, kosmos, 2016-02-01, Mine)
#!duplicate key value violates unique constraint "schedule_slot_telescope_f1e499ac_uniq"
#!DETAIL:  Key (telescope, instrument, obsdate)=(kp4m, kosmos, 2016-02-01) already exists.'''
#!        self.assertEqual(expected, response.content.decode())
        
    #!def test_upload(self):
    #!    test_file = '/var/mars/small.xml'
    #!    with open(test_file, 'rb') as fp:
    #!        request = self.factory.post('/schedule/upload/',
    #!                                    {'xmlfile': fp,
    #!                                     'comment': 'for UNIT TEST'})
    #!    response = schedule.views.upload_file(request)
    #!    tele = 'ct4m'
    #!    date = '2014-01-01'
    #!    slot = Slot.objects.get(obsdate=date, telescope=tele)
    #!    propid = slot.propid
    #!    expected = '2012B-0001'
    #!    #!self.assertRedirects(response, reverse('schedule:list'))
    #!    self.assertEqual(response.status_code, 302)
    #!    self.assertEqual(propid, expected)
    
    #!def test_list(self):
    #!    request = self.factory.get('/schedule/list/')
    #!    response = schedule.views.SlotList.as_view()(request)
    #!    self.assertEqual(200, response.status_code)
    #!    self.assertContains(response,'2013B-0142')
