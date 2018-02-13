"""\
Database Access Layer
All external access of the database should come through the functions
in this module.
"""

import logging
import json
from os import path
import coreapi
import jsonschema
from django.db import connections
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views.decorators.http import require_POST, require_http_methods

from rest_framework import response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from natica.models import FilePrefix
from natica.views import process_search
from astropy.coordinates import SkyCoord

from . import exceptions as dex
from .serializers import FilePrefixSerializer


# curl -H "Content-Type: application/json" -X POST -d @search-1.json http://localhost:8080/natica/search/ | python -m json.tool
@api_view(['POST'])
@require_POST
def search_by_json(request):
    """
    Search Archive for matches against supplied JSON.
    Response: FITS metadata (header field/values).
    """
    return process_search(request)

@csrf_exempt
@api_view(['GET'])
def tele_inst_pairs(request):  # # @Portal
    """
    Retrieve all valid telescope/instrument pairs.
    Determined by TADA file prefix table.

    Response will be an array of **telescope**, **instrument** pairs

    `[ [\"telescope1\", \"instrument1\"], [\"telescope2\", \"instrument2\"] ]`
    """
    qs = FilePrefix.objects.all().order_by('pk').values('telescope',
                                                        'instrument')
    serialized = FilePrefixSerializer(qs, many=True)
    return JsonResponse([(d['telescope'],d['instrument'])
                         for d in list(serialized.data)],
                         safe=False)


@csrf_exempt
def get_categories_for_query(request):  # @Portal
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
        sql1 = ('SELECT {}, count(*) as total  FROM voi.siap {} group by {}'.format(category, where_clause, indx))
        cursor.execute(sql1)
        categories[indx] = utils.dictfetchall(cursor)

    resp = {"status":"success", "categories":categories}
    return JsonResponse(resp, safe=False)


@csrf_exempt
@api_view(['GET'])
def object_lookup(request): # @Portal
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
    return response.Response(schema)
