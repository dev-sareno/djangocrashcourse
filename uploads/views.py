from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse, HttpResponseNotFound
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.core.files.storage import default_storage


class UploadResponse:
    status_code = None
    status = None

    def __init__(self, status_code, status):
        self.status_code = status_code
        self.status = status

    def to_json(self):
        return self.__dict__

    def __setitem__(self, idx, value):
        self.__dict__[idx] = value


@csrf_exempt
def upload_json(request: HttpRequest):
    if request.method == 'POST':
        # validate file
        if 'file' not in request.FILES:
            return HttpResponse('not found: file', status=400)

        file_param = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file_param.name, file_param)
        uploaded_file_url = fs.url(filename)

        # file_path = os.path.join(settings.BASE_DIR, uploaded_file_url)
        file_path = "%s%s" % (settings.BASE_DIR, uploaded_file_url)
        file = default_storage.open(file_path)
        data = file.read()  # bytes
        file.close()

        json_string = data.decode("utf-8")
        json_ob = json.loads(json_string)

        response = UploadResponse(1, 'Successful')
        response['path'] = uploaded_file_url
        response['path_sys'] = file_path
        response['data'] = json_ob

        return JsonResponse(response.to_json(), status=200)
    else:
        return Http404()
