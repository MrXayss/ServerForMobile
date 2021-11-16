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

@csrf_exempt
@require_POST
def upload_image(request):
    z = json.loads(request.body.decode('utf-8'))
    print("POST:",json.dumps(request.body.decode('utf-8')))
    print(z["coord1"])
    return HttpResponse(request)