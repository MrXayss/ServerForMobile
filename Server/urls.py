"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import show_info,download_file,delete_data,show_traffic,show_specific_traffic,right_trafiic,bad_traffic,login,start_page,logout,check_login,right_trafiic_main,bad_traffic_main,date_accelerometer

urlpatterns = [
    # path('upload_image', upload_image, name='upload_image'),
    path("api/", include('api.urls')),
    path("admin/",admin.site.urls),
    # path(r'', show_info,name='admin'),
    path(r'', show_info,name='admin'),
    path('login/', login,name='login'),
    path('login/check_login/', check_login,name='check_login'),
    path('logout/', logout,name='logout'),
    path('traffic/', show_traffic,name='traffic'),
    path('download/<slug:pk>', download_file, name='download_file'),
    path('delete/<slug:pk>', delete_data, name='delete_data'),
    path('traffic_info/<slug:pk>', show_specific_traffic, name='show_specific_traffic'),
    path('traffic_right/<slug:pk>', right_trafiic, name='right_trafiic'),
    path('traffic_bad/<slug:pk>', bad_traffic, name='bad_traffic'),
    path('traffic_right_main/<slug:pk>', right_trafiic_main, name='right_trafiic_main'),
    path('traffic_bad_main/<slug:pk>', bad_traffic_main, name='bad_traffic_main'),
    path('date_accelerometer/', date_accelerometer, name='date_accelerometer'),
]
