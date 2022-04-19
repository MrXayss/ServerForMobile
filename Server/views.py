from django.shortcuts import render, redirect
import logging
import base64
import binascii
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden,FileResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.template import loader
from api.models import InfoTrafficLight
import os
import mimetypes
import codecs
from PIL import Image
from django.shortcuts import get_object_or_404
from pathlib import Path


# @csrf_exempt
# @require_POST
# def upload_image(request):
#     z = json.loads(request.body.decode('utf-8'))
#     print("POST:",json.dumps(request.body.decode('utf-8')))
#     print(z["coord1"])
#     return HttpResponse(request)

def show_phones(request):
    InfoTrafficLight1 = InfoTrafficLight.objects.order_by('id')
    template = loader.get_template('admin.html')
    context = {
        'InfoTrafficLight_list': InfoTrafficLight1,
    }
    return HttpResponse(template.render(context, request))


def download_file(request, pk):
    my_object = get_object_or_404(InfoTrafficLight, id=pk)
    attach = request.GET.get("attach", False)
    try:
        return FileResponse(
            open(Path("media") / my_object.photo.name, "rb"), as_attachment=attach
        )
    except FileNotFoundError:
        return HttpResponseNotFound("File not found %s" % my_object.id)

def delete_data(request, pk):
    record = InfoTrafficLight.objects.get(id = pk)
    os.remove(Path("media") / str(record.photo))
    record.delete()
    return redirect(show_phones)
