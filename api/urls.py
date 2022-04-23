from django.urls import path

from .views import upload_image,test_upload

app_name = 'api'

urlpatterns = [
    path('upload_image', upload_image, name='upload_image'),
    path('test_upload', test_upload, name='test_upload'),
]