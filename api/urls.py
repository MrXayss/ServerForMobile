from django.urls import path

from .views import upload_image

app_name = 'api'

urlpatterns = [
    path('upload_image', upload_image, name='upload_image'),
    
]