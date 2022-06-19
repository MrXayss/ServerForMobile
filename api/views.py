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
def check_location(request):
    data_get = json.loads(request.body.decode('utf-8'))
    points = {}
    for i in TrafficLight.objects.all():
        dist = 6371.01 * acos(sin(radians(data_get['Latitude']))*sin(radians(i.latitude)) + cos(radians(data_get['Latitude']))*cos(radians(i.latitude))*cos(radians(data_get['Longitude']) - radians(i.longtitude)))
        if (round(dist*1000) <=5):
            print("Ближайший светофор:", i.id)
            points[i.id]=dist*1000
    if (points =={}):
        return_data ='0-0'
        return HttpResponse(return_data)
    else:
        return_data = str(int(TrafficLight.objects.get(id = min(points,key=points.get)).gradus))+'-'+str(min(points,key=points.get))
        return HttpResponse(return_data)

count = 0

@csrf_exempt
@require_POST
def upload_image(request):
    global count 
    count = count + 1
    global id_traffic
    id_traffic = request.POST["text_loc"]
    if (count < 3 ):
        file = request.FILES['record']
        new_entry = TrafficLight(gradus=request.POST["gradus"], latitude=request.POST["latitude"], longtitude=request.POST["longtitude"],photo=file,id_device=request.POST["id_device"],signal =request.POST["text_signal"],location=TraficLightName.objects.get(id=id_traffic))    #**z)
        new_entry.save()
        b = json.loads(request.POST["json"])
        new_entry = DateOfAccelerometer(x=b['x'], y=b['y'], z=b['z'],traffic=TrafficLight.objects.latest('id'))
        new_entry.save()
    else:
        count = 0 
        file = request.FILES['record']
        new_entry = TrafficLight(gradus=request.POST["gradus"], latitude=request.POST["latitude"], longtitude=request.POST["longtitude"],photo=file,id_device=request.POST["id_device"],signal =request.POST["text_signal"],location=TraficLightName.objects.get(id=id_traffic))    #**z)
        new_entry.save()
        json_data = json.loads(request.POST["json"])
        new_entry = DateOfAccelerometer(x=json_data['x'], y=json_data['y'], z=json_data['z'],traffic=TrafficLight.objects.latest('id'))
        new_entry.save()
        list_traffic =list(TrafficLight.objects.filter(location=TraficLightName.objects.latest('id').id))
        latitude_average = 0
        longtitude_average = 0
        count_data = 0
        gradus_average = 0
        for i in list_traffic:
            latitude_average = latitude_average+i.latitude
            longtitude_average = longtitude_average+i.longtitude
            gradus_average = gradus_average+i.gradus
            count_data = count_data+1
        new_entry = TraficLightName.objects.filter(id=request.POST["text_loc"]).update(latitude=latitude_average/count_data,longtitude=longtitude_average/count_data,gradus=float(ceil(gradus_average/count_data)))
    return HttpResponse(request)
