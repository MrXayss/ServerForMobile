from django.shortcuts import render
import logging
import base64
import binascii
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from api.models import InfoTrafficLight

@csrf_exempt
@require_POST
def upload_image(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(z["coord1"])
    new_entry = InfoTrafficLight(gradus=z["gradus"], latitude=z["coord1"], longtitude=z["coord2"])    #**z)
    new_entry.save()
    return HttpResponse(request)

@csrf_exempt
@require_POST
def test_upload(request):
    print("Файл: ",request.FILES["record"])
    print("Градусы: ",request.POST["gradus"])
    print("Широта: ",request.POST["latitude"])
    print("Долгота: ",request.POST["longtitude"])
    new_entry = InfoTrafficLight(gradus=request.POST["gradus"], latitude=request.POST["latitude"], longtitude=request.POST["longtitude"],photo=request.FILES["record"])    #**z)
    new_entry.save()
    file_name = str(request.FILES["record"])
    handle_uploaded_file(
        request.FILES["record"], file_name
    )
    return HttpResponse(request)

def handle_uploaded_file(file, filename):
    with open("api/uploads/" + filename, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)