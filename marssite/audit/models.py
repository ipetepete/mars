from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.utils.html import format_html
#from django.contrib.postgres.fields import HStoreField
from natica.models import Site,Telescope,Instrument
from django.forms import model_to_dict

#!  fstops = [
#!    'dome',
#!    'mountain:dropbox', 'mountain:queue',
#!    'mountain:cache', 'mountain:anticache`',
#!    'valley:dropbox',   'valley:queue',
#!    'valley:cache',   'valley:anticache',
#!    'archive']
#!
#!    errcodes = ['DUPFITS', 'BADPROP', 'COLLIDE', 'NOPROP', 'MISSREQ',
#!                'BADDATE', 'NOFITS', 'UNKNOWN', 'none']
#!
#!telescopes = ('bok23m,aat,ct09m,ct13m,ct15m,ct1m,ct4m,'
#!              'gem_n,gem_s,gemn,gems,het,'
#!              'keckI,keckII,kp09m,kp13m,kp21m,kp4m,kpcf,'
#!              'magI,magII,mmt,soar,wiyn,unknown').split(',')
#!instruments = ['arcoiris', '90prime',  'mosaic3', 'ccd_imager'] + sorted([
#!    'mop/ice', 'arcon', 'spartan', 'decam',
#!    'falmingos', 'gtcam', 'wildfire', 'chiron',
#!    'osiris', 'andicam', 'echelle', 'flamingos',
#!    'sam', 'newfirm', 'goodman', 'y4kcam', 'minimo/ice', 'ice',
#!    'ispi', 'mosaic', 'goodman spectrograph', 'hdi', 'bench',
#!    'kosmos', 'spartan ir camera', 'soi', '(p)odi', 'whirc',
#!    'cosmos',  'unknown'])


class AuditRecord(models.Model):
    # Field values provided by DOME
    md5sum = models.CharField(max_length=40, primary_key=True, db_index=True,
                              help_text='MD5SUM of FITS file')
    obsday = models.DateField(null=True, # allow no Dome info, only Submit
                              help_text='Observation Day')
    telescope = models.ForeignKey(Telescope)
    instrument = models.ForeignKey(Instrument)    
    srcpath = models.CharField(max_length=256, 
                               help_text='Path of file as submitted')
    fstop_host =  models.CharField(max_length=40, blank=True,
                                  help_text='Host name of more recent fstop')
    
    # Field values automatically filled in (was called "recorded")
    updated  = models.DateTimeField(default=timezone.now,
                                     help_text='When AuditRecord updated')

    ##### Field values added by TADA
    fstop = models.CharField(max_length=25, blank=True,
                             help_text = 'Most downstream stop of FITS file')
    
    submitted = models.DateTimeField(blank=True, null=True,
                                     help_text='When submitted to archive')
    success   = models.NullBooleanField(
        help_text=('Null until ingest attempted.'
                   'Then True iff Archive reported success on ingest'))
    archerr   = models.CharField(max_length=256, blank=True,
                                 help_text='Archive ingest error message')
    errcode   = models.CharField(max_length=10, blank=True,
                                 default='',
                                 help_text=(
                                     'Error code for error reported from'
                                     ' dataq, tada, archive'))

    archfile  = models.CharField(max_length=80, blank=True,
                                 help_text='Basename of FITS file in Archive')
    metadata = JSONField(blank=True, null=True,
                           help_text='FITS metadata changed by ingest')

    ##### Field values used for bookkeeping (by DART)
    staged   = models.BooleanField(
        default=False,
        help_text=('Marked for subsequent action.'))
    hide   = models.BooleanField(
        default=False,
        help_text=('Exclude these records in audit reports.'))

    
    def narrow_srcpath(self):
        return format_html(
            '<span style="color: green; width: 10px;">{}</span>',
            self.srcpath,
        )
            
#!    def __str__(self):
#!        return '{}-{}'.format(self.obsday, self.instrument)

 
    #!class Meta:
    #!    ordering = ('telescope','instrument','srcpath')
        
        
