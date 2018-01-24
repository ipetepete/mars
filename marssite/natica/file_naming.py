import datetime as dt
from pathlib import PurePath
import logging
from natica.models import FilePrefix,ObsType,ProcType,ProdType

def fits_extension(fname):
    '''Return extension of any file matching <basename>.fits.*, basename.fits
Extension may be: ".fits.fz", ".fits", ".fits.gz", etc'''
    _, ext = os.path.splitext(fname)
    if ext != '.fits':
        _, e2  = os.path.splitext(_)
        ext = e2 + ext
    return ext[1:]

    
def generate_archive_path(hdr, ext='.fits.fz', tag=None):
    site = hdr.get('DTSITE','nota').lower()
    telescope = hdr.get('DTTELESC','nota').lower()
    instrument = hdr.get('DTINSTRU','nota').lower()
    obstype = hdr.get('OBSTYPE', 'nota').lower()
    proctype = hdr.get('PROCTYPE', 'nota').lower()
    prodtype = hdr.get('PRODTYPE', 'nota').lower()
    serno = hdr.get('DTSERNO')
    # e.g. DATEOBS='2002-12-25T00:00:00.000001'
    obsdt = dt.datetime.strptime(hdr.get('DATE-OBS','NA'),
                                 '%Y-%m-%dT%H:%M:%S.%f')
    date = obsdt.date().strftime('%y%m%d')
    time = obsdt.time().strftime('%H%M%S')

    flavor = ''
    if serno != None:
        flavor += '_s{serno}'
    if (tag != None) and (tag != ''):
        flavor += '_t{tag}'

    #fpqs = FilePrefix.objects.filter(site='kp',telescope='wiyn',instrument='whirc')
    fpqs = FilePrefix.objects.filter(site=site,telescope=telescope,instrument=instrument)
    obsqs = ObsType.objects.filter(name=obstype)
    procqs = ProcType.objects.filter(name=proctype)
    prodqs = ProdType.objects.filter(name=prodtype)
    fnfields = dict(
        prefix=(fpqs[0].prefix if len(fpqs)>0 else 'uuuu'),
        date=date,
        time=time,
        obstype=obsqs[0].code if len(obsqs)>0 else 'u',
        proctype=procqs[0].code if len(procqs)>0 else 'u',
        prodtype=prodqs[0].code if len(prodqs)>0 else 'u',
        flavor=flavor, # optional (may be null string)
        ext=ext,
        )

    std='{prefix}_{date}_{time}_{obstype}{proctype}{prodtype}{flavor}{ext}'
    basename=std.format(**fnfields)
    archive_path = PurePath('/data/natica-archive', # archive_root
                            hdr['DTCALDAT'].replace('-',''),
                            hdr['DTTELESC'],
                            hdr['DTPROPID'],
                            basename)
    return archive_path
             
