from django.shortcuts import render
import logging
import base64
import binascii
from datetime import datetime
from django.http import  HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from api.models import InfoTrafficLight,TraficLightName
from math import radians, sin, cos, acos

@csrf_exempt
@require_POST
def upload_image(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(z['name_traffic'])
    new_entry = TraficLightName(name_trafficlight = z['name_traffic'])
    new_entry.save()
    a=TraficLightName.objects.latest('id').id
    return HttpResponse(a)

@csrf_exempt
@require_POST
def check_location(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(type(z['Latitude']))
    a = {}
    for rack in InfoTrafficLight.objects.all():
        slat = radians(61.2490)
        slon = radians(73.3820)
        elat = radians(61.2493369)
        elon = radians(73.3840201)
        # dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        dist = 6371.01 * acos(sin(radians(z['Latitude']))*sin(radians(rack.latitude)) + cos(radians(z['Latitude']))*cos(radians(rack.latitude))*cos(radians(z['Longitude']) - radians(rack.longtitude)))
        print(dist*1000)
        if (round(dist*1000) <=5):
            print("Ближайший светофор:", rack.id)
            a[rack.id]=dist*1000
        # print(round(dist, 5))
    print(a)
    print("vby -",min(a,key=a.get))
    print("sas -",int(InfoTrafficLight.objects.get(id = min(a,key=a.get)).gradus))
    sas = int(InfoTrafficLight.objects.get(id = min(a,key=a.get)).gradus)
    # print(min(income, key=income.get))
    return HttpResponse(sas)

@csrf_exempt
@require_POST
def test_upload(request):
    # print("12: ",request.POST["json"])
    b = json.loads(request.POST["json"])
    # print("Файл: ",request.FILES["record"])
    # print("Градусы: ",request.POST["gradus"])
    # print("Широта: ",request.POST["latitude"])
    # print("Долгота: ",request.POST["longtitude"])
    # print("Устройство: ",request.POST["id_device"])
    # print("Сигнал: ",request.POST["text_signal"])
    a = request.POST["text_loc"]
    print("Сообщение:",a)
    file = request.FILES['record']
    new_entry = InfoTrafficLight(gradus=request.POST["gradus"], latitude=request.POST["latitude"], longtitude=request.POST["longtitude"],photo=file,json=b,id_device=request.POST["id_device"],signal =request.POST["text_signal"],location=TraficLightName.objects.get(id=a))    #**z)
    new_entry.save()
    # file_name = str(datetime.now())
    # handle_uploaded_file(
    #     request.FILES["record"], file_name
    # )s
    # file_name = default_storage.save(file.name, file)
    return HttpResponse(request)
