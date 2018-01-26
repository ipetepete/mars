"""For LSA query handling
"""
from collections import OrderedDict
from pprint import pformat
from . import exceptions as dex
from django.db import connections
from django.conf import settings
import datetime

response_fields = '''
    reference,
    ra,
    dec,
    prop_id,
    surveyid as survey_id,
    date_obs as obs_date,
    dtpi as pi,
    telescope,
    instrument,
    release_date,
    rawfile as flag_raw,
    proctype,
    filter,
    filesize,
    filename,
    dtacqnam as original_filename,
    md5sum,
    exposure,
    obstype as observation_type,
    obsmode as observation_mode,
    prodtype as product,
    proctype,
    seeing,
    depth
'''



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def remove_leading(thestring, lead):
    """Remove LEAD from left of THESTRING if its there."""
    if thestring.startswith(lead):
        return thestring[len(lead):]
    return thestring

def db_float_range(range_value, field):
    """range_value:: [minVal, maxVal, bounds]
    see: https://www.postgresql.org/docs/9.3/static/functions-range.html
    """
    if isinstance(range_value, list):
        # contains element (postresql SQL)
        # '[2011-01-01,2011-03-01)'::tsrange @> '2011-01-10'::timestamp
        # If the third argument is omitted, '[)' is assumed.
        #
        # INclusive bound :: "(", ")"
        # EXclusive bound :: "[", "]"
        minval,maxval,*xtra = range_value
        bounds = xtra[0] if (len(xtra) > 0) else '[)'
        clause = (" AND ('{}{},{}{}'::numrange @> {})"
                  .format(bounds[0], minval, maxval, bounds[1], field))
    else:
        clause = " AND ({} = '{}')".format(field, range_value)
    return clause

def db_time_range(range_value, field):
    # Edge case bugs!!!
    if isinstance(range_value, list):
        # contains element (postresql SQL)
        # '[2011-01-01,2011-03-01)'::tsrange @> '2011-01-10'::timestamp
        # If the third argument is omitted, '[)' is assumed.
        #
        # INclusive bound :: "(", ")"
        # EXclusive bound :: "[", "]"
        mindate,maxdate,*xtra = range_value
        bounds = xtra[0] if (len(xtra) > 0) else '[)'
        clause = (" AND ('{}{},{}{}'::tsrange @> {}::timestamp)"
                  .format(bounds[0], mindate, maxdate, bounds[1], field))
    else:
        clause = " AND ({} = '{}')".format(field, range_value)
    return clause

def db_null(field):
    clause = " AND (({} is null) OR ({} = ''))".format(field, field)
    return clause

def db_exact(value, field):
    clause = " AND ({} = '{}')".format(field, value)
    return clause

def db_oneof(value_list, field):
    clause = ""
    for val in value_list:
        clause += " OR ({} = '{}')".format(field, val)
    return ' AND (' + remove_leading(clause, ' OR ') + ')'

def db_ti_oneof(value_list):
    clause = ""
    frag = ""
    try:
        for telescope,instrument in value_list:
            clause += " OR ((telescope = '{}') AND (instrument = '{}'))" \
                       .format(telescope, instrument)
        frag = ' AND (' + remove_leading(clause, ' OR ') + ')'
    except Exception as err:
        raise dex.BadTIFormat(
            'search.telescope_instrument but be list of form: '
            '[["tele1", "instrum1"], ["t2","i2"]]')
    return frag

proc_LUT = dict(raw = 'raw',
                calibrated = 'InstCal',
                reprojected = 'projected',
                stacked = 'stacked',
                master_calibration = 'mastercal',
                image_tiles = 'tiled',
                sky_subtracted = 'skysub')

def process_query(jsearch, page, page_limit, order_fields, return_where_clause=False):
    """
    Processing of the query
        jsearch         - json query
        page            - natural number index of page
        page_limit      - limit of results
        order_fields    - a string of fieldnames to order by: separated by space
    """
    #!print("DBG: Process Query using db host '{}'".format(settings.DATABASES['archive']['HOST']))
    #!print('DBG: settings.DATABASES = {}'.format(pformat(settings.DATABASES)))
    limit_clause = 'LIMIT {}'.format(page_limit)
    offset = (page-1) * page_limit
    offset_clause = 'OFFSET {}'.format(offset)
    order_clause = ('ORDER BY ' +
                    ', '.join(['{} {}'.format(f[1:], ('DESC'
                                                      if f[0]=='-' else 'DESC'))
                               for f in order_fields.split()]))
    avail_fields = set([
        'search_box_min',
        'pi',
        'prop_id',
        'obs_date',
        'filename',
        'original_filename',
        'telescope_instrument',
        'observation_type',
        'observation_mode',
        'survey_id',
        'release_date',
        'flag_raw',
        'image_filter',
        'exposure_time',
        'coordinates',
    ])
    used_fields = set(jsearch.keys())
    if not (avail_fields >= used_fields):
        unavail = used_fields - avail_fields
        #print('DBG: Extra fields ({}) in search'.format(unavail))
        raise dex.UnknownSearchField('Extra fields ({}) in search'.format(unavail))
    assert(avail_fields >= used_fields)

    # Query Legacy Science Archive
    cursor = connections['archive'].cursor()
    # Force material view refresh
    cursor.execute('SELECT * FROM refresh_voi_material_views()')  #@@@
    where = '' # WHERE clause innards

    slop = jsearch.get('search_box_min', .001)
    if 'coordinates' in jsearch:
        coord = jsearch['coordinates']
        where += ((' AND (ra <= {}) AND (ra >= {})'
                    ' AND (dec <= {}) AND (dec >= {})')
                    .format(coord['ra'] + slop,
                            coord['ra'] - slop,
                            coord['dec'] + slop,
                            coord['dec'] - slop))
    if 'pi' in jsearch:
        pi = jsearch['pi']
        if pi is None or pi is '':
            where += db_null('dtpi')
        else:
            where += db_exact(pi, 'dtpi')
    if 'prop_id' in jsearch:
        prop_id = jsearch['prop_id']
        if prop_id is None or prop_id is '':
            where += db_null('dtpropid')
        else:
            where += db_exact(prop_id, 'dtpropid')
    if 'obs_date' in jsearch:
        where += db_time_range(jsearch['obs_date'], 'date_obs')
    if 'filename' in jsearch:
        where += db_exact(jsearch['filename'], 'dtnsanam')
    if 'original_filename' in jsearch:
        where += db_exact(jsearch['original_filename'], 'dtacqnam')
    if 'observation_type' in jsearch:
        obstype = jsearch['observation_type']
        if obstype is None or obstype is '':
            where += db_null('obstype')
        else:
            where += db_exact(obstype, 'obstype')
    if 'observation_mode' in jsearch:
        obsmode = jsearch['observation_mode']    
        if obsmode is None or obsmode is '':
            where += db_null('obsmode')
        else:
            where += db_exact(obsmode, 'obsmode')
    if 'survey_id' in jsearch:
        surveyid = jsearch['survey_id']
        if surveyid is None or surveyid is '':
            where += db_null("surveyid")
        else:
            where += db_exact(jsearch['survey_id'], 'surveyid')
    #!if 'telescope' in jsearch:
    #!    where += db_oneof(jsearch['telescope'], 'telescope')
    #!if 'instrument' in jsearch:
    #!    where += db_oneof(jsearch['instrument'], 'instrument')
    # NEW api (0.1.7): "telescope_instrument":[["ct4m", "cosmos"], ["soar","osiris"]]
    if 'telescope_instrument' in jsearch:
        where += db_ti_oneof(jsearch['telescope_instrument'])
    if 'release_date' in jsearch:
        where += db_time_range(jsearch['release_date'], 'release_date')
    if 'flag_raw' in jsearch:
        where += db_exact(jsearch['flag_raw'], 'rawfile')
    if 'image_filter' in jsearch:
        where += db_oneof([proc_LUT[p] for p in jsearch['image_filter']],
                            'proctype')
    if 'exposure_time' in jsearch:
        where += db_float_range(jsearch['exposure_time'], 'exposure')

    where = remove_leading(where, ' AND ')
    #!print('DBG-2 where="{}"'.format(where))
    where_clause = '' if len(where) == 0 else 'WHERE {}'.format(where)

    if return_where_clause:
        return where_clause

    #@@@sql0 = 'SELECT count(reference) FROM voi.siap {}'.format(where_clause)
    #!print('DBG-6: search_by_json; sql0=',sql0)
    cursor.execute(sql0)
    total_count = cursor.fetchone()[0]

    #@@@sql = ('SELECT {} FROM voi.siap {} {} {} {}'
    #@@@        .format(' '.join(response_fields.split()),
    #@@@                where_clause,
    #@@@                order_clause,
    #@@@                limit_clause,
    #@@@                offset_clause  ))
    #!print('DBG-2 sql={}'.format(sql))
    #!print('DBG-2.1 cursor={}'.format(cursor))
    cursor.execute(sql)
    results = dictfetchall(cursor)


    #print('DBG results={}'.format(results))
    meta = OrderedDict.fromkeys(['dal_version',
                                    'timestamp',
                                    'comment',
                                    'sql',
                                    'page_result_count',
                                    'to_here_count',
                                    'total_count'])
    meta.update(
        dal_version = dal_version,
        timestamp = datetime.datetime.now(),
        comment = (
            'WARNING: Has not been tested much.'
            ' Does not use IMAGE_FILTER.'
        ),
        sql = sql,
        page_result_count = len(results),
        to_here_count = offset + len(results),
        total_count = total_count,
    )
    resp = OrderedDict.fromkeys(['meta','resultset'])
    resp.update( meta = meta, resultset = results)
    return resp
