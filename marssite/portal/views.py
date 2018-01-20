from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.conf import settings
from shutil import copyfile
from os import path
#from siap import queries
from . import utils
import datetime
import tempfile
from dal import externals as dalx
import time
import hashlib
import zipfile
import os
import json
import requests
import logging

"""
Assume there are some mount points on this machine
one will have the archive files
another will have the ftp directories

This needs to get a list of files (selected by the user) and create
relative os.symlinks from the archive to the ftp directory owned by the user
"""

logger = logging.getLogger(__name__)
ftpdirs = "/srv/ftp"

# This is where the nfs mount exists inside this container/vm etc.
# the path returned for each archive resource needs to be changed
# to check if the file exists etc
nfsmount = ""
ftppasswd = "/srv/ftp/ftp-passwd/pureftpd.passwd"
dev = os.environ.get('ENVIRONMENT', False)

missingFiles = []


def _link_file(fname, uname):
    userdir = os.path.join(ftpdirs, 'anon', uname)
    if os.path.isdir(userdir) == False:
        os.mkdir(userdir)
    #!nfspath = queries.get_fits_location(fname)
    filepath = nfsmount + nfspath

    # make the file for testing
    if dev:
        _make_dev_file(filepath)
    try:
        if False == os.path.isfile(nfsmount + nfspath):
            missingFiles.append(fname)
            return False
        os.symlink(nfsmount + nfspath, "{}/{}".format(userdir,fname))
    except:
        # error is always present, not sure why...
        pass
    return fname


def _make_dev_file(filepath):
    # create directories if not already made
    dirs = os.path.dirname(filepath).split("/")[1:]
    dirs.insert(0, "/")
    storagepath = nfsmount
    logger.debug("STAGING:Making temp dev file in: {}".format(filepath))
    for dr in dirs:
        storagepath = os.path.join(storagepath,dr)
        if os.path.isdir(storagepath) == False:
            os.mkdir(storagepath)

    f= open(filepath, 'w')
    f.write("the filename is {}".format(filepath))

    # adjust the actual file pathname location to match mounted location
    f.close()
    logger.debug("----- file made")



def dir_sorter(elem):
    dir = elem.split("_")
    if len(dir) < 2:
        return 0
    if dir[1].isdigit() == False:
        return 0
    return int(dir[1])

def get_user_name(request):
    if request.session.get('username', False):
        return request.session['username']
    dirs = os.listdir("/srv/ftp/anon")
    if len(dirs) == 0:
        nextdir = 0
    else:
        topdir = sorted(dirs, key=dir_sorter, reverse=True)[0]
        nextdir = int(topdir.split("_")[1])

    name = "user_{}".format(nextdir + 1)
    logger.info("STAGING:NEWUSERCREATED:{}".format(name))
    request.session['username'] = name
    return name

@csrf_exempt
def download_selected(request):
    message = ""
    if len(request.body) > 0:
        data = json.loads(request.POST.get("selected","[]"))
        # create a zip for download
        # limit to 10 files
        logger.debug("STAGING:DOWNLOAD:{} Files requested:{}".format(len(data), get_user_name(request)))
        tmp = tempfile.NamedTemporaryFile(delete=False)
        zf = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
        for f in data[:10]:
            #!fpath = nfsmount+queries.get_fits_location(f['file']['reference'])
            zf.write(os.path.abspath(fpath), f['file']['reference'])

        zf.close()

        size = tmp.tell()
        tmp.seek(0)
        os.chmod(tmp.name, 0o666)
        logger.debug("STAGING:ZIPFILE:{}".format(", ".join(os.listdir("/tmp"))))
        response = HttpResponse("", content_type="application/zip")
        response['Content-Disposition'] = "attachement; filename={}".format(get_user_name(request)+".zip")
        response['Content-Length'] = size

        response['X-Accel-Redirect'] = os.path.join("/download/zip", os.path.basename(tmp.name))
        return response

    else:
        return JsonResponse({'message':'Error, no data provided', 'status':'error'})

    # ftp directories mounted at /srv/ftp

    # check if user loggedin, put links in user dir - get from ldap

    # otherwise generate a guest user directory in the anonymous ftp
    # directory
    return JsonResponse({'message':'ok', 'status':'ok'})

def download_single_file(request):
    filename = request.GET.get('f', '')
    filepath = nfsmount
    #!filepath += queries.get_fits_location(filename)
    logger.debug("STAGING:DOWNLOADSIGNLEFILE:{}".format(filepath))
    if dev:
        _make_dev_file(filepath)
    response = HttpResponse('',content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Accel-Redirect'] = "/download/archive/"+filepath.replace("/net/archive/mtn", "")
    return response

# create the lookup paths for the various js resources
def _get_resources(appname):
    # get the resource names for html
    curdir = os.path.dirname(__file__)
    resPath = os.path.join(curdir,"../static/portal/dist")
    stats = open(path.join(curdir, "webpack-assets.json"), 'r')
    resources = json.loads(stats.read())
    r = []

    # manifest & app are removed and added in proper order here because order matters at load time
    r.append(resources.pop('manifest')['js'])
    app = resources.pop(appname)
    for js in resources:
        if js.find("bundle") > -1:
            # skip the unwanted app code
            continue
        r.append(resources[js]['js'])
    r.append(app['js'])
    return r

def search(request):
    r = _get_resources("app.bundle")
    return render(request, "search.html", {"jsResources":r })

"""
  Staging will setup either all the resultset or as selected subset based on a get variable
  @get(stage) ["all", "selected"]
  @post(selectedFiles) - When staging subset
"""
@csrf_exempt
def staging(request):
    message = ""
    """
    Are we staging a subset or the entire result set?
    """
    stageAll = True if request.GET.get("stage", "") == "all" else False

    if stageAll:
        # Load the page, it will then do an ajax callback to generate the links
        #
        pass
    else:
        fileList = request.POST.get("selectedFiles")
        if len(fileList) > 0:
            data = json.loads(fileList)
            for record in data:
                _link_file(record['reference'], get_user_name(request))
        else:
            response = render_to_response('500.html', {"message":"No files were selected"},
                                    context_instance=RequestContext(request))
            response.status_code = 500
            return response


    r = _get_resources("staging.bundle")

    return render(request, "staging.html", {'jsResources':r})


@csrf_exempt
def stageall(request):
    # get the query used to generate the last result set
    # save the query in the user's session to pull it back out
    # iterate through the results to generate links
    body = request.body.decode('utf-8')

    try:
        postdata = json.loads(body)

    except:
        return JsonResponse({"message":"No/invalid data, original search data could not be parsed", "status":"error"})


    # create links for the entire result set
    # call dal's external...
    fnames = dalx.get_all_filenames_for_query(postdata)
    stagedfiles = []
    for ref in fnames:
       file = _link_file(ref, get_user_name(request))
       if file:
           stagedfiles.append(file)

    return JsonResponse({'total_files':len(stagedfiles), 'missing_files':missingFiles})


    # get the file list from dal
