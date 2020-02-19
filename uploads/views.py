from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, Http404, JsonResponse, HttpResponseNotFound
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


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
        if not request.FILES['file']:
            return HttpResponse('not found: file', status=400)

        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        response = UploadResponse(1, 'Successful')
        response['path'] = uploaded_file_url

        return JsonResponse(response.to_json(), status=200)
    else:
        return Http404()
