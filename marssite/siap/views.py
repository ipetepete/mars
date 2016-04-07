import json

from django.db import connection
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.views.generic.list import ListView
from django.core.context_processors import csrf
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


from .models import Image, VoiSiap
from .queries import get_tada_references

def index(request):
    'SIAP index of subset of all files.'
    limit=250
    sql = 'SELECT count(*) FROM voi.siap;'
    sql2='SELECT * FROM voi.siap LIMIT {}'.format(limit) #!!! not all
    from django.db import connection
    #!cursor = connection.cursor()
    #!cursor.execute( sql )
    #!total = cursor.fetchone()[0]
    context = RequestContext(request, {
        #!'total_image_count': total,
        'limit_count': limit,
        'recent_image_list': Image.objects.raw(sql2) ,
    })

    return render(request, 'siap/index.html', context)

# Regex search takes almost 20 seconds to search 11.3 million records
def tada(request): 
    'List of SIAP files containing TADA in Archive filename.'
    limit = 2000
    images = get_tada_references(limit=limit)
    #! images = [r[0] for r in cursor.fetchall()]
    #!for im in images:
    #!    print('Image={}'.format(im))
    print('request.content_type={}'.format(request.META.get('CONTENT_TYPE')))
    
    context = RequestContext(request, {
        'limit_count': limit,
        'tada_images': images, # Image.objects.raw(sql),
    })

    if request.META.get('CONTENT_TYPE','none') == 'application/json':
        return JsonResponse([im[0] for im in images], safe=False)
    if request.META.get('CONTENT_TYPE','none') == 'text/csv':
        import csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tada.csv"'
        writer = csv.writer(response)
        for im in images:
            writer.writerow(im)
        return response
    else:
        return render(request, 'siap/tada.html', context)
    
def getnsa(request, dtacqnam):
    sql='SELECT dtnsanam FROM voi.siap WHERE dtacqnam = %s'
    obs = Image.objects.raw(sql,[dtacqnam])
    return HttpResponse(obs[0], content_type='text/plain')

def getacq(request, dtnsanam):
    sql='SELECT dtacqnam FROM voi.siap WHERE dtnsanam = %s'
    obs = Image.objects.raw(sql,[dtnsanam])
    return HttpResponse(obs[0], content_type='text/plain')

def filenames(request, propid):
    context = RequestContext(request, {
        'propid': propid,
        'image_list': Image.objects.raw("SELECT * FROM voi.siap  WHERE prop_id = %s",[propid])
    })
    return render(request, 'siap/filenames.html', context)

class FileListView(ListView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        context['image_list'] = Image.objects.raw("SELECT * FROM voi.siap  WHERE prop_id = %s",[propid])


        return context    

def detail(request, image_id):
    #!im = get_object_or_404(Image, pk=image_id)
    im_list = (Image.objects
               .raw("SELECT * FROM voi.siap WHERE reference = %s", [image_id]))
    context = RequestContext(request, {
        #!'dict': im.__dict__,
        'dict': im_list[0].__dict__,
    })
    return render(request, 'siap/detail.html', context)

# NB: raw SQL is string with FORMATTING PARAMETERS so '%' indicates paramter.
#     Double any occurances to protect from interpretation.
# curl -H "Content-Type: application/json" -X POST -d '{"sql":"xyz","bitcoins":"100"}' http://localhost:8000/siap/arch/query
#
# cat <<EOF > foo.json
# {"sql":"SELECT * FROM voi.siap WHERE reference LIKE '%%TADA%%' ", "bitcoins":"100"}
# EOF
# curl -H "Content-Type: application/json" -X POST -d @foo.json http://localhost:8000/siap/arch/query
#@api_view(['POST'])
@csrf_exempt
def query_by_json(request, format='json'):
    'Upload a file constaining SQL that does a SELECT against SIAP table.'
    print('EXECUTING: views<siap>:query_by_file')
    # Easy way to test post???
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        print('body={}'.format(body))
        sql = body['sql']
        cursor = connection.cursor()
        # Force material view refresh
        cursor.execute('SELECT * FROM refresh_voi_material_views()') 
        cursor.fetchall()
        cursor.execute( sql )
        total = cursor.rowcount
        results = cursor.fetchall()
        #print('results={}'.format(results))
        qs = VoiSiap.objects.raw(sql)
        
    #!c = {'form': form}
    #!c.update(csrf(request))
    resdict = dict(sql=sql, results=list(results))
    print('resdict={}'.format(resdict))
    print('qs={}'.format(list(qs)))
    #return JsonResponse(dict(sql=sql, results=list(results), ))
    #return JsonResponse(serializers.serialize('json', qs), safe=False)
    print('serialized results={}'.format(serializers.serialize(format, qs)))
    return JsonResponse(serializers.serialize(format, qs), safe=False)
