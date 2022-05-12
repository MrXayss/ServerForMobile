from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,FileResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.template import loader
from api.models import InfoTrafficLight,TraficLightName
import os
from django.shortcuts import get_object_or_404
from pathlib import Path
from django.contrib import auth
from django.contrib.auth.models import User


# @csrf_exempt
# @require_POST
# def upload_image(request):
#     z = json.loads(request.body.decode('utf-8'))
#     print("POST:",json.dumps(request.body.decode('utf-8')))
#     print(z["coord1"])
#     return HttpResponse(request)

def show_info(request):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        InfoTrafficLight1 = InfoTrafficLight.objects.order_by('id')
        template = loader.get_template('admin.html')
        context = {
            'InfoTrafficLight_list': InfoTrafficLight1,
        }
        return HttpResponse(template.render(context, request))

def show_traffic(request):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        InfoTrafficLight1 = TraficLightName.objects.order_by('id')
        inf1 = InfoTrafficLight.objects.filter(location_id=19)
        print(inf1)
        template = loader.get_template('traffic.html')
        context = {
            'InfoTrafficLight_list': InfoTrafficLight1,
        }
        return HttpResponse(template.render(context, request))

def show_specific_traffic(request, pk):
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        inf1 = InfoTrafficLight.objects.filter(location_id=pk)
        template = loader.get_template('trafficinfo.html')
        context = {
            'InfoTrafficLight_list': inf1,
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
    if not request.user.is_authenticated:
        return redirect(login)
    else:
        record = InfoTrafficLight.objects.get(id = pk)
        os.remove(Path("media") / str(record.photo))
        record.delete()
        return redirect(show_info)

def right_trafiic(request, pk):
    InfoTrafficLight.objects.filter(id=pk).update(status=False)
    return redirect(show_info)

def bad_traffic(request, pk):
    InfoTrafficLight.objects.filter(id=pk).update(status=True)
    return redirect(show_info)

def login(request):
    template = loader.get_template('login.html')
    context = {
        'error': '',
    }
    return HttpResponse(template.render(context, request))

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

def start_page(request):
    template = loader.get_template('login.html')
    context = {
        'InfoTrafficLight_list': 'sas',
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    auth.logout(request)
    return redirect(show_info)