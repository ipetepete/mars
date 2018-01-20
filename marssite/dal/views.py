import json
from os import path
import coreapi
import jsonschema
from django.db import connections
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from natica.models import FilePrefix
from astropy.coordinates import SkyCoord

from . import exceptions as dex
from . import utils
from .serializers import FilePrefixSerializer

dal_version = '0.1.7' # MVP. mostly untested

utils.dal_version = dal_version

#    object as object_name,          -- object_name
COMMENTED_response_fields = '''
    reference,
    ra,
    dec,
    prop_id,
    surveyid as survey_id,          -- survey_id
    date_obs as obs_date,           -- obs_date
    dtpi as pi,                     -- pi
    telescope,
    instrument,
    release_date,
    rawfile as flag_raw,            -- flag_raw ???
    proctype,
    filter,
    filesize,
    filename,
    dtacqnam as original_filename,  -- original_filename
    md5sum,
    exposure,
    obstype as observation_type,    -- observation_type
    obsmode as observation_mode,    -- observation_mode
    prodtype as product,            -- product ???
    proctype,
    seeing,
    depth
'''


def fake_error_response(request, error_type):
    fake_err_types = ['bad_numeric',
                      'bad_search_json',
    ]
    if error_type == 'bad_numeric':
        raise dex.BadNumeric('Bad numeric value')
    elif error_type == 'bad_search_json':
        raise dex.BadSearchSyntax('Invalid JSON for search. Bad syntax.')
    else:
        raise dex.BadFakeError(
            'Unknown value ({}) for URL ERROR parameter. Allowed: {}'
            .format(error_type, ','.join(fake_err_types)))



## Under PSQL, copy SELECTed results to CSV using:
#
# \copy (SELECT * from voi.siap WHERE (ra <= 186.368791666667) AND (ra >= 176.368791666667) AND (dec <= -40.5396111111111) AND (dec >= -50.5396111111111) AND (dtpi = 'Cypriano') AND (dtpropid = 'noao') AND ('[2009-04-01,2009-04-03]'::tsrange @> date_obs::timestamp) AND (dtacqnam = '/ua84/mosaic/tflagana/3103/stdr1_012.fits') AND ((telescope = 'ct4m') OR (telescope = 'foobar')) AND ((instrument = 'mosaic_2')) AND (release_date = '2010-10-01T00:00:00') AND ((proctype = 'raw') OR (proctype = 'InstCal')) AND (exposure = '15')) TO '~/data/metadata-dal-2.csv'

# curl -H "Content-Type: application/json" -X POST -d @fixtures/search-sample.json http://localhost:8000/dal/search/ > ~/response.json
# curl -H "Content-Type: application/json" -X POST -d @request.json http://localhost:8000/dal/search/ | python -m json.tool
@csrf_exempt
def search_by_json(request, query=None):
    """
    Search the NOAO Archive, returns a list of image resource metadata.
    **Context**

    ``query``
        Payload satisfying /etc/mars/search-schema.json .
    """
    #!print('DBG-0: search_by_json')
    gen_error = request.GET.get('error',None)
    if gen_error != None:
        return fake_error_response(request, gen_error)


    # !!! Verify values (e.g. telescope) are valid. Avoid SQL injection hit.
    page_limit = int(request.GET.get('limit','100')) # num of records per page
    page = int(request.GET.get('page','1'))
    # order:: comma delimitied, leading +/-  (ascending/descending)
    order_fields = request.GET.get('order','+reference')

    #!print('EXECUTING: views<dal>:search_by_file; method={}, content_type={}'
    #!      .format(request.method, request.content_type))
    if request.method == 'POST':
        #root = ET.Element('search')
        #!print('DBG body str={}'.format(request.body.decode('utf-8')))
        if request.content_type == "application/json":
            if query != None:
                jsearch = query
            else:
                jsearch = json.loads(request.body.decode('utf-8'))
            # Validate against schema
            try:
                schemafile = path.join(settings.BASE_DIR, "dal", "fixtures", "search-schema.json")
                with open(schemafile) as f:
                    schema = json.load(f)
                    jsonschema.validate(jsearch, schema)
            except Exception as err:
                raise dex.BadSearchSyntax('JSON did not validate against /etc/mars/search-schema.json'
                                          '; {}'.format(err))

        else:
            raise dex.CannotProcessContentType('Cannot parse content type: {}'
                                               .format(request.content_type))

        resp = utils.process_query(jsearch, page, page_limit, order_fields)
        return JsonResponse(resp)

    elif request.method == 'GET':
        return HttpResponse('Requires POST with json payload')

@csrf_exempt
def staging(request):
    query = ""
    # check if files exist
    query = json.loads(request.body.decode('utf-8'))
    res = search_by_json(request, query)



@csrf_exempt
@api_view(['GET'])
def tele_inst_pairs(request):
    """
    Retrieve all valid telescope/instrument pairs.
    Determined by TADA file prefix table.

    Response will be an array of **telescope**, **instrument** pairs

    `[ [\"telescope1\", \"instrument1\"], [\"telescope2\", \"instrument2\"] ]`
    """
    qs = FilePrefix.objects.all().order_by('pk').values('telescope',
                                                        'instrument')
    serialized = FilePrefixSerializer(qs, many=True)
    return JsonResponse([(d['telescope'],d['instrument']) for d in list(serialized.data)],
                         safe=False)

@csrf_exempt
def get_categories_for_query(request):
    """
    Get a list of unique values for the following columns:
    Proposal Id, Survey Id, PI, Telescope, instrument, filter, observation type,
    observation mode, processing, product
    """
    # get uniques for filters
    query = json.loads(request.body.decode('utf-8'))
    cursor = connections['archive'].cursor()
    category_fields = [
        "prop_id",
        "surveyid as survey_id",
        "dtpi as pi",
        "concat(telescope, ',', instrument) as telescope_instrument",
        "filter",
        "obstype as observation_type",
        "obsmode as observation_mode",
        "prodtype as product",
        "proctype as processing"
    ]

    where_clause = utils.process_query(jsearch=query, page=1, page_limit=50000, order_fields='', return_where_clause=True)
    categories = {}
    for category in category_fields:
        indx = category.split(" as ").pop()
        #@@@sql1 = ('SELECT {}, count(*) as total  FROM voi.siap {} group by {}'.format(category, where_clause, indx))
        cursor.execute(sql1)
        categories[indx] = utils.dictfetchall(cursor)

    resp = {"status":"success", "categories":categories}
    return JsonResponse(resp, safe=False)


@csrf_exempt
@api_view(['GET'])
def object_lookup(request):
    """
    Retrieve the RA,DEC coordinates for a given object by name.
    """
    obj_name = request.GET.get("object_name", "")
    obj_coord = SkyCoord.from_name(obj_name)
    return JsonResponse({'ra':obj_coord.ra.degree, 'dec':obj_coord.dec.degree})


###
# API Schema Metadata
schema = coreapi.Document(
    title="Search API",
    url="http://localhost:8000",

    content={
        "search": coreapi.Link(
            url="/dal/search/",
            action = "post",
            fields = [
                coreapi.Field(
                    name="obs_date",
                    required=False,
                    location="form",
                    description="Single date or date range"
                ),
                coreapi.Field(
                    name="prop_id",
                    required=False,
                    location="form",
                    description="Prop ID to search for"
                ),
                coreapi.Field(
                    name="pi",
                    required=False,
                    location="form",
                    description="Principle Investigator"
                ),
                coreapi.Field(
                    name="filename",
                    required="false",
                    location="form",
                    description="Ingested archival filename"
                )
            ],
            description='''
            NOAO Search API

Requests need to be wrapped in a root `search` paramater

            {
              \"search\":{
                 \"obs_date\":\"2015-09-06\"
              }
            }
            '''
        )
    }
)

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    '''
      Search API
    '''
    #generator = schema.SchemaGenerator(title='Bookings API')
    #return Response(generator.get_schema())
    return response.Response(schema)
