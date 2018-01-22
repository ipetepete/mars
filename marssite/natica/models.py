'''For eventual replacement of legacy Science Archive DB'''

from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField, DateRangeField, FloatRangeField

class Site(models.Model):
    name = models.CharField(max_length=10, primary_key=True,
                            help_text='Site (mountain)')
    def __str__(self): return self.name

class Telescope(models.Model):
    name = models.CharField(max_length=10, primary_key=True,
                            help_text=('Name used in FITS header '
                                       '(field name TELES'))
    def __str__(self): return self.name

class Instrument(models.Model):
    name = models.CharField(
        max_length=20, primary_key=True,
        help_text=('Name used in FITS header (field name INSTRUME)'))

    def __str__(self): return self.name

class TacInstrumentAlias(models.Model):
    """Map TAC instrument name to NATICA instrument"""
    tac = models.CharField(max_length=20, primary_key=True,
                           help_text='Name used by TAC Schedule')
    hdr = models.ForeignKey(Instrument,
                            on_delete=models.CASCADE,
                            help_text='Name used in FITS header')

class Proposal(models.Model):
    extras = JSONField()
    prop_id = models.CharField(null=True, max_length=10, unique=True)
    pi = models.CharField(max_length=40)
    proprietary_period = models.SmallIntegerField() # months

    def __str__(self):
        return ("{}({}): {}"
                .format(self.prop_id, self.proprietary_period, self.pi))

class FitsFile(models.Model):
    extras = JSONField(default={})  
    # md5sum of file as stored in MSS
    md5sum = models.CharField(max_length=32, unique=True)
    filesize  = models.BigIntegerField()
    proposal = models.ForeignKey(Proposal, null=True, on_delete=models.SET_NULL)

    ############################################
    ### Fields that LSA Portal can query against
    # We never want User or Archive pathnames to be truncated. So allow
    # unlimitted text length.  MAX_LENGTH is just for auto-gen forms.
    original_filename = models.TextField(max_length=30)
    archive_filename = models.TextField(max_length=30)
    # calibration images might have to be stored. No RA, DEC for those.
    ra = FloatRangeField(null=True, help_text='RA min,max')
    dec = FloatRangeField(null=True, help_text='DEC min,max')
    #
    exposure = FloatRangeField()
    #!prodtype = models.CharField(max_length=8)
    date_obs = DateRangeField(null=True, help_text='DATE-OBS min,max')
    #pi = models.CharField(max_length=40)
    #prop_id = models.CharField(max_length=10)
    release_date     = models.DateField()
    
    #!instrument = models.CharField(max_length=80, help_text="INSTRUME")
    #!telescope = models.CharField(max_length=80, help_text="TELESCOP")
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    
    ###
    ############################################
    

class Hdu(models.Model):
    """Required header fields per FITS Std 3.0"""
    # Other FITS field content not stored below
    extras = JSONField() 

    fitsfile = models.ForeignKey(FitsFile, on_delete=models.CASCADE)
    hdu_idx  = models.PositiveSmallIntegerField() # hdu_idx[0] :: Primary HDU
    # (SIMPLE = T) Required For Primary HDU
    # name of ext type; Required For Conformant Extensions HUD
    xtension = models.CharField(max_length=40, blank=True)

    # Required For Primary, Extension HDU
    bitpix = models.IntegerField()
    naxis = models.PositiveSmallIntegerField()
    naxisN = ArrayField(models.PositiveSmallIntegerField(), default=list)#!!!
    
    # Required For Conformant Extensions HDU (not Primary)
    pcount = models.PositiveIntegerField(null=True)
    gcount = models.PositiveIntegerField(null=True)

    # Others (not required by Standard, but we need them in at least one HDU)
    #
    #!instrument =models.CharField(max_length=80,blank=True,help_text="INSTRUME")
    #!telescope  =models.CharField(max_length=80,blank=True,help_text="TELESCOP")
    #!date_obs  = models.DateTimeField(null=True, help_text = 'DATE-OBS')
    #!obj  = models.CharField(max_length=80, blank=True, help_text = 'OBJECT')
    #!# RA,DEC in dms e.g. "16:18:37.00"
    #!ra = models.CharField(null=True, max_length=20) 
    #!dec = models.CharField(null=True, max_length=20) 




    
##############################################################################
### Used in creating Standard NOAO filenames for the archive.
### See: http://ast.noao.edu/sites/default/files/File_Naming_Conventions_v12.pdf
###   "File Naming Convention for the NOAO Science Archive"
###   October 1, 2014

# Replaces tada/file_naming.py:stiLUT{}
class FilePrefix(models.Model):
    """Archive filename prefix coded from Site, Telescope, Instrument"""

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    telescope = models.ForeignKey(Telescope, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=10,
                              help_text='Prefix for Archive Filename')
    comment = models.CharField(max_length=80, blank=True, default='')

class ObsType(models.Model):
    """OBServation type: used archive filename prefix"""
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=1, unique=False)
    comment = models.CharField(max_length=80, blank=True, default='')

class ProcType(models.Model):
    """PROCessing type: used archive filename prefix"""
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=1, unique=False)
    comment = models.CharField(max_length=80, blank=True, default='')
    def __str__(self): return self.name
    
class ProdType(models.Model):
    """PRODuct type: used archive filename prefix"""
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=1, unique=False)
    comment = models.CharField(max_length=80, blank=True, default='')
    def __str__(self): return self.name


###
##############################################################################

