from django.db import models
from django.contrib.postgres.fields import ArrayField

class Site(models.Model):
    name = models.CharField(max_length=10, unique=True,
                            help_text='Site (mountain)')
    def __str__(self): return self.name

class Telescope(models.Model):
    name = models.CharField(max_length=10,  unique=True,
                            help_text=('Name used in FITS header '
                                       '(field name TELES'))
    def __str__(self): return self.name



class TacInstrumentAlias(models.Model):
    tac = models.CharField(max_length=20, unique=True,
                           help_text='Name used by Dave Bells TAC Schedule')
    hdr = models.CharField(max_length=20, unique=True,
                           help_text='Name used in FITS header')

    
class Instrument(models.Model):
    name = models.CharField(
        max_length=20, unique=True,
        help_text=('Name used in FITS header (field name INSTRUME)'))

    def __str__(self): return self.name

#!class InstrumentAlias(models.Model):
#!    reason = models.CharField(max_length=80)
#!    #!instrument = models.ForeignKey(Instrument)

# Replaces tada/file_naming.py:stiLUT{}
class FilePrefix(models.Model):
    """Archive filename prefix coded from Site, Telescope, Instrument"""

    site = models.ForeignKey(Site)
    telescope = models.ForeignKey(Telescope)
    instrument = models.ForeignKey(Instrument)
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

class ProdType(models.Model):
    """PRODuct type: used archive filename prefix"""
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=1, unique=False)
    comment = models.CharField(max_length=80, blank=True, default='')

###########

class RawKeywords(models.Model):
    """All bets are off in the original FITS file does not contain all of these.
    (RAW_REQUIRED_FIELDS in tada:fits_utils.py)
    """
    name = models.CharField(max_length=8, unique=True)
    comment = models.CharField(max_length=80, blank=True, default='')

class FilenameKeywords(models.Model):
    """These fields are required to construct the Archive filename and path.
Some may be common with INGEST_REQUIRED.
(FILENAME_REQUIRED_FIELDS in tada:fits_utils.py)
"""
    name = models.CharField(max_length=8, unique=True)
    comment = models.CharField(max_length=80, blank=True, default='')

class IngestKeywords(models.Model):
    """To be able to ingest a fits file into the (NOAO Science) archive,
all of these must be present in the header.
# The commented out lines are Requirements per document, but did not seem to
# be required in Legacy code.
(INGEST_REQUIRED_FIELDS in tada:fits_utils.py)
    """
    name = models.CharField(max_length=8, unique=True)
    comment = models.CharField(max_length=80, blank=True, default='')

class IngestRecommendedKeywords(models.Model):
    """We should try to fill these fields were practical. They are used
in the archive. Under the portal they may affect ability to query or
show as the results of queries.  If any of these are missing just
before ingest, a warning will be logged indicating the missing fields.
(INGEST_RECOMMENDED_FIELDS in tada:fits_utils.py)
    """
    name = models.CharField(max_length=8, unique=True)
    comment = models.CharField(max_length=80, blank=True, default='')

###########

class SupportKeywords(models.Model):
    """Fields used in hdr_calc_funcs.py
(SUPPORT_FIELDS in tada:fits_utils.py)
    """
    name = models.CharField(max_length=8, unique=True)
    comment = models.CharField(max_length=80, blank=True, default='')

class FloatKeywords(models.Model):
    """Fields to force into FLOAT format during FITS scrub. The FITS
standard requires these to be floats, but in practice some fields are
strings so this list does not contain full list of FITS standard
requirements.
(FLOAT_FIELDS in tada:fits_utils.py)
    """
    name = models.CharField(max_length=8, unique=True)
    comment = models.CharField(max_length=80, blank=True, default='')
    
##################################################################

class HdrFunc(models.Model):
    """Definition of FITS header Mapping Functions previously in
hdr_calc_funcs.py  Each function has a signature of: 
FUNC(orig, **kwargs): return NEW
where 'orig' is orginal header as a dictionary. Returns NEW defined as dictionary used to update the header.
    """
    name = models.CharField(max_length=40, unique=True,
                            help_text='Function name as used in personality.')
    documentation = models.TextField(max_length=120, blank=True, 
                                     help_text='Function description.')
    definition = models.TextField(help_text='Python function BODY' )
    inkeywords = ArrayField(
        models.CharField(max_length=8,
                         help_text='FITS keywords needed by func'),
        default=list)
    outkeywords = ArrayField(
        models.CharField(
            max_length=8,
            help_text='FITS keywords added or modified by func'),
        default=list )

    
