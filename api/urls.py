from django.urls import path

from .views import upload_image,check_location

app_name = 'api'

urlpatterns = [
    path('upload_image', upload_image, name='upload_image'),
    path('check_location', check_location, name='check_location'),
]