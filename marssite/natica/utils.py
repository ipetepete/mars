"""\
Convenience functions for NATICA.
"""
import logging
import json
import jsonschema

from . import exceptions as nex
from . import search_filters as sf

search_fields = set([
    'search_box_min',
    'coordinates',
    'pi',
    'prop_id',
    'obs_date',
    'filename',
    'original_filename',
    'telescope_instrument',
    'release_date',
    'flag_raw',
    'image_filter',
    'exposure_time',
    #'xtension', # new
    'extras',
])


def make_qobj(jsearch):
    """Construct Q object (anchored on FitsFile) that matches
search given in jsearch (JSON format)."""
    
    #####################################
    ### Validate input

    # Insure jsearch matches schema
    try:
        schemafile = '/etc/mars/search-schema.json'
        with open(schemafile) as f:
            schema = json.load(f)
            jsonschema.validate(jsearch, schema)
    except Exception as err:
        raise nex.SearchSyntaxError(
            'JSON did not validate against {}; {}'
            .format(schemafile, err))

    # Insure only allowed fields are present
    #!used_fields = set(jsearch.keys())
    #!if not (search_fields >= used_fields):
    #!    unavail = used_fields - search_fields
    #!    raise nex.ExtraSearchFieldError('Extra fields ({}) in search'
    #!                                 .format(unavail))
    #assert(search_fields >= used_fields)
    
    slop = jsearch.get('search_box_min', .001)
    q = (sf.coordinates(jsearch.get('coordinates', None), slop)
         & sf.exposure_time(jsearch.get('exposure_time', None))  
         & sf.archive_filename(jsearch.get('filename', None))
         & sf.image_filter(jsearch.get('image_filter', None))
         & sf.dateobs(jsearch.get('obs_date', None))
         & sf.original_filename(jsearch.get('original_filename', None))
         & sf.pi(jsearch.get('pi', None))
         & sf.prop_id(jsearch.get('propid', None))
         & sf.release_date(jsearch.get('release_date', None))
         & sf.telescope_instrument(jsearch.get('telescope_instrument', None))
         )
         #& sf.extras(jsearch.get('extras', None))
         #& sf.xtension(jsearch.get('xtension', None))
    #!q = (sf.telescope_instrument(jsearch.get('telescope_instrument', None))   )
    logging.debug('DBG: q={}'.format(str(q)))
    return q # Q object
