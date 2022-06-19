from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,FileResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.template import loader
from api.models import TrafficLight,TraficLightName,UserRoles,DateOfAccelerometer,Devices
import os
from django.shortcuts import get_object_or_404
from pathlib import Path
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin



def show_info(request):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        print(request.user.id)
        if (UserRoles.objects.get(id_user_id=request.user.id).is_information_collector == True):
            role = "is_information_collector"
            InfoTrafficLight1 = TrafficLight.objects.filter(id_device=Devices.objects.get(user=request.user.id).device).order_by('id')
            template = loader.get_template('admin.html')
            context = {
                'InfoTrafficLight_list': InfoTrafficLight1,"role":role
            }
            return HttpResponse(template.render(context, request))
        elif (UserRoles.objects.get(id_user_id=request.user.id).is_handler == True):
            role = "is_handler"
            InfoTrafficLight1 = TraficLightName.objects.order_by('id')
            template = loader.get_template('traffic.html')
            context = {
                'InfoTrafficLight_list': InfoTrafficLight1,
            }
            return HttpResponse(template.render(context, request))
        elif (UserRoles.objects.get(id_user_id=request.user.id).is_admin == True):
            role = "is_admin"
            InfoTrafficLight1 = TrafficLight.objects.order_by('id')
            template = loader.get_template('admin.html')
            context = {
                'InfoTrafficLight_list': InfoTrafficLight1,"role":role
            }
            return HttpResponse(template.render(context, request))


def show_traffic(request):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        if (UserRoles.objects.get(id_user_id=request.user.id).is_information_collector == True):
            return redirect(show_info)
        elif (UserRoles.objects.get(id_user_id=request.user.id).is_admin == True or UserRoles.objects.get(id_user_id=request.user.id).is_handler == True):
            InfoTrafficLight = TraficLightName.objects.order_by('id')
            template = loader.get_template('traffic.html')
            context = {
                'InfoTrafficLight_list': InfoTrafficLight,
            }
            return HttpResponse(template.render(context, request))

def show_specific_traffic(request, pk):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        if (UserRoles.objects.get(id_user_id=request.user.id).is_information_collector == True):
            return redirect(show_info)
        elif (UserRoles.objects.get(id_user_id=request.user.id).is_admin == True or UserRoles.objects.get(id_user_id=request.user.id).is_handler == True):
            inf1 = TrafficLight.objects.filter(location_id=pk)
            template = loader.get_template('trafficinfo.html')
            context = {
                'InfoTrafficLight_list': inf1,
            }
            return HttpResponse(template.render(context, request))


def download_file(request, pk):
    my_object = get_object_or_404(TrafficLight, id=pk)
    attach = request.GET.get("attach", False)
    try:
        return FileResponse(
            open(Path("media") / my_object.photo.name, "rb"), as_attachment=attach
        )
    except FileNotFoundError:
        return HttpResponseNotFound("File not found %s" % my_object.id)

def delete_data(request, pk):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
            record = TrafficLight.objects.get(id = pk)
            os.remove(Path("media") / str(record.photo))
            record.delete()
            return redirect(show_info)

def date_accelerometer(request):
    inf = DateOfAccelerometer.objects.order_by('id')
    template = loader.get_template('accelerometer.html')
    context = {
        'InfoTrafficLight_list': inf,
    }
    return HttpResponse(template.render(context, request))

def right_trafiic(request, pk):
    TrafficLight.objects.filter(id=pk).update(status=False)
    return redirect(show_info)

def bad_traffic(request, pk):
    TrafficLight.objects.filter(id=pk).update(status=True)
    return redirect(show_info)

def right_trafiic_main(request, pk):
    TraficLightName.objects.filter(id=pk).update(status=False)
    return redirect(show_info)

def bad_traffic_main(request, pk):
    TraficLightName.objects.filter(id=pk).update(status=True)
    return redirect(show_info)

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def check_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(show_info)
        else:
            return redirect(login)

def logout(request):
    auth.logout(request)
    return redirect(show_info)