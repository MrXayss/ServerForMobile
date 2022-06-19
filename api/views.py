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
from api.models import TrafficLight,TraficLightName,DateOfAccelerometer
from math import radians, sin, cos, acos,ceil

@csrf_exempt
@require_POST
def upload_image(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(z['name_traffic'])
    new_entry = TraficLightName(name_trafficlight = z['name_traffic'])
    new_entry.save()
    a1=TraficLightName.objects.latest('id').id
    return HttpResponse(a1)

@csrf_exempt
@require_POST
def check_location(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(type(z['Latitude']))
    a1 = {}
    for rack in TrafficLight.objects.all():
        # dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        dist = 6371.01 * acos(sin(radians(z['Latitude']))*sin(radians(rack.latitude)) + cos(radians(z['Latitude']))*cos(radians(rack.latitude))*cos(radians(z['Longitude']) - radians(rack.longtitude)))
        print(dist*1000)
        if (round(dist*1000) <=5):
            print("Ближайший светофор:", rack.id)
            a1[rack.id]=dist*1000
        # print(round(dist, 5))
    if (a1 =={}):
        sas ='0-0'
        return HttpResponse(sas)
    else:
        print("vby -",min(a1,key=a1.get))
        print("sas -",int(TrafficLight.objects.get(id = min(a1,key=a1.get)).gradus))
        sas = str(int(TrafficLight.objects.get(id = min(a1,key=a1.get)).gradus))+'-'+str(min(a1,key=a1.get))
        print(sas)
        return HttpResponse(sas)

count = 0

@csrf_exempt
@require_POST
def test_upload(request):
    global count 
    count = count + 1
    global a
    a = request.POST["text_loc"]
    print("Сообщение:",a)
    if (count < 3 ):
        file = request.FILES['record']
        new_entry = TrafficLight(gradus=request.POST["gradus"], latitude=request.POST["latitude"], longtitude=request.POST["longtitude"],photo=file,id_device=request.POST["id_device"],signal =request.POST["text_signal"],location=TraficLightName.objects.get(id=a))    #**z)
        new_entry.save()
        b = json.loads(request.POST["json"])
        new_entry = DateOfAccelerometer(x=b['x'], y=b['y'], z=b['z'],traffic=TrafficLight.objects.latest('id'))
        new_entry.save()
    else:
        count = 0 
        file = request.FILES['record']
        new_entry = TrafficLight(gradus=request.POST["gradus"], latitude=request.POST["latitude"], longtitude=request.POST["longtitude"],photo=file,id_device=request.POST["id_device"],signal =request.POST["text_signal"],location=TraficLightName.objects.get(id=a))    #**z)
        new_entry.save()
        b = json.loads(request.POST["json"])
        new_entry = DateOfAccelerometer(x=b['x'], y=b['y'], z=b['z'],traffic=TrafficLight.objects.latest('id'))
        new_entry.save()
        cc =list(TrafficLight.objects.filter(location=TraficLightName.objects.latest('id').id))
        p = 0
        p1 = 0
        c1 = 0
        p2 = 0
        for i in cc:
            p = p+i.latitude
            p1 = p1+i.longtitude
            p2 = p2+i.gradus
            c1 = c1+1
        print(p/c1,p1/c1)
        print(c1)
        new_entry = TraficLightName.objects.filter(id=request.POST["text_loc"]).update(latitude=p/c1,longtitude=p1/c1,gradus=float(ceil(p2/c1)))
    # file_name = str(datetime.now())
    # handle_uploaded_file(
    #     request.FILES["record"], file_name
    # )s
    # file_name = default_storage.save(file.name, file)
    return HttpResponse(request)
