from django.db import models
from django.contrib.postgres.fields import ArrayField
from natica.models import Site,Telescope,Instrument

class EmptySlot(models.Model):
    #!telescope = models.CharField(max_length=80)
    #!instrument = models.CharField(max_length=20)
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    obsdate = models.DateField()
    modified = models.DateTimeField(auto_now=True, help_text='When modified' )

    class Meta:
        unique_together = ('telescope', 'instrument', 'obsdate')
        index_together = ['telescope', 'instrument', 'obsdate']

    def __str__(self):
        return '{}:{}-{}'.format(self.obsdate, self.telescope, self.instrument)
        
class Proposal(models.Model):
    propid = models.CharField(primary_key=True,  max_length=10,
                              help_text='YYYYs-nnnn (s[emester]:: A|B)')

    #!title = models.CharField(max_length=256)
    #!pi_name = models.CharField(max_length=80,
    #!                           help_text='Principal Investigator name')
    #!pi_affiliation = models.CharField(max_length=160)
    modified = models.DateTimeField(auto_now=True, help_text='When modified')
    
    def __str__(self):
        return self.propid

class DefaultPropid(models.Model):
    #!telescope = models.CharField(max_length=10)
    #!instrument = models.CharField(max_length=20)
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)    

    propids = ArrayField( models.CharField(max_length=10) )
    

#!    # These are the only telescopes allowed by the perl script that
#!    # uses a foreign web service for schedule retrieval.  Since the web
#!    # service will return error for anything else, we limit also.
#!    telescopes = ('aat,ct09m,ct13m,ct15m,ct1m,ct4m,gem_n,gem_s,gemn,gems,het,'
#!                  'keckI,keckII,kp09m,kp13m,kp21m,kp4m,kpcf,'
#!                  'magI,magII,mmt,soar,wiyn').split(',')
#!    instruments = ('mosaic3', 'mop/ice', 'arcon', 'spartan', 'decam',
#!                   '90prime', 'falmingos', 'gtcam', 'wildfire', 'chiron',
#!                   'osiris', 'arcoiris', 'andicam', 'echelle', 'flamingos',
#!                   'sam', 'newfirm', 'goodman', 'y4kcam', 'minimo/ice', 'ice',
#!                   'ispi', 'mosaic', 'goodman spectrograph', 'hdi', 'bench',
#!                   'kosmos', 'spartan ir camera', 'soi', '(p)odi', 'whirc',
#!                   'cosmos', 'biw')


class Slot(models.Model):
    # THESE ONLY GET UPDATED when django is started.
    #telescopes = [obj.name for obj in Telescope.objects.all()]
    #instruments = [obj.name for obj in Instrument.objects.all()]
    #!telescope = models.CharField(max_length=10)
    #!instrument = models.CharField(max_length=20)
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)    

    obsdate = models.DateField(help_text='Observation date') # DATE-OBS

    proposals = models.ManyToManyField(Proposal)
    modified = models.DateTimeField(auto_now=True, help_text='When modified' )
    frozen = models.BooleanField(default=False,
                                 help_text=('Protect against changing this '
                                            'slot during a bulk operation.'))

    split = models.BooleanField(
        default=True,
        help_text=(
            'Iff TRUE treat a slot as Split Night '
            '(hdr propid must be in schedule lists)'))
    
    def propid_list(self):
        #! return ', '.join([p.propid for p in self.proposals.all()[:4]])
        return ', '.join([p.propid for p in self.proposals.all()])

    propids = property(propid_list)
    
    def __str__(self):
        return '{}:{}-{}'.format(self.obsdate, self.telescope, self.instrument)
        
    #!pi_name = models.CharField(max_length=80,
    #!                           help_text='Principal Investigator name')
    #!pi_affiliation = models.CharField(max_length=160)
    #!title = models.CharField(max_length=256)
    #!
    class Meta:
        unique_together = ('telescope', 'instrument', 'obsdate')
        index_together = ['telescope', 'instrument', 'obsdate']
        


class SlotSet(models.Model):
    xmlfile = models.FileField(upload_to='mars/%Y%m%d/schedule.xml')
    comment = models.CharField(max_length=256, blank=True)

