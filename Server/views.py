from django.shortcuts import render
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


@csrf_exempt
@require_POST
def upload_image(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(z["coord1"])
    return HttpResponse(request)

def show_phones(request):
    InfoTrafficLight1 = InfoTrafficLight.objects.order_by('id')
    a = str([60.421875, 60.4375, 61.046875, 61.046875, 61.046875, 61.765625, 61.828125, 61.84375, 62.3125, 62.359375, 62.359375, 62.375, 62.234375, 62.234375, 62.234375, 62.03125, 62.03125, 62.03125, 61.796875, 61.765625, 61.765625, 61.640625, 61.625, 61.625, 61.625, 61.625, 61.625, 61.625, 61.734375, 61.734375, 61.921875, 61.953125, 61.953125, 62.234375, 62.265625, 62.265625, 62.265625, 62.53125, 62.546875, 62.5625, 62.5625, 62.71875, 62.71875, 62.734375, 62.953125, 62.953125, 62.953125, 63.046875, 63.046875, 63.046875, 63.078125, 63.09375, 63.09375, 63.09375, 63.328125, 63.34375, 63.34375, 63.34375, 63.34375, 63.34375, 63.359375, 63.359375, 63.359375, 63.46875, 63.46875, 63.484375, 63.484375, 63.421875, 63.40625, 63.40625, 63.53125, 63.484375, 63.484375, 63.59375, 63.59375, 63.65625, 63.765625, 63.765625, 63.96875, 63.984375, 64.03125, 64.109375, 64.109375, 64.15625, 64.125, 64.125, 64.09375, 64.0625, 64.0625, 64.078125, 64.078125, 64.09375, 64.09375, 64.09375, 64.046875, 64.046875, 64.046875, 64.0625, 64.0625, 64.0625, 64.09375, 64.09375, 64.09375, 64.03125, 64.03125, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 63.984375, 63.984375, 64.015625, 64.046875, 64.046875, 64.046875, 64.0625, 64.078125, 64.09375, 64.21875, 64.21875, 64.21875, 64.765625, 64.8125, 64.8125, 65.546875, 65.609375, 65.609375, 65.625, 66.640625, 66.640625, 66.65625, 67.34375, 67.421875, 67.421875, 67.8125, 67.84375, 67.84375, 67.796875, 67.78125, 67.78125, 67.78125, 67.609375, 67.609375, 67.609375, 67.4375, 67.4375, 67.4375, 67.21875, 67.1875, 67.1875, 67.0625, 67.046875, 67.046875, 67.046875, 67.0, 67.0, 67.0, 66.921875, 66.921875, 66.8125, 66.8125, 66.8125, 66.734375, 66.734375, 66.734375, 66.5625, 66.5625, 66.53125, 66.40625, 66.40625, 66.390625, 66.390625, 66.234375, 66.21875, 66.21875, 65.984375, 65.953125, 65.953125, 65.90625, 65.890625, 65.890625, 65.890625, 65.890625, 66.0, 66.0, 66.0, 66.109375, 66.109375, 66.125])
    print(len(a))
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
        return HttpResponseNotFound("File not found %s" % my_object.name)