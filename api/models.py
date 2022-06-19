from datetime import datetime
from email.policy import default
from django.db import models
from django.forms import BooleanField
from django.contrib.auth.models import User

class TraficLightName(models.Model):
    name_trafficlight = models.CharField(max_length=100, verbose_name="Название перекрестка", default='0')
    latitude = models.FloatField(max_length=100,verbose_name="Долгота",null=True)
    longtitude = models.FloatField(max_length=100,verbose_name="Широта",null=True)
    gradus = models.FloatField(max_length=100,verbose_name="Градусы",null=True)
    status = models.BooleanField(verbose_name="Айди устройства", null=True)

class TrafficLight(models.Model):
    id_device = models.CharField(max_length=100, verbose_name="Айди устройства", default='0')
    gradus = models.FloatField(max_length=100,verbose_name="Градусы")
    latitude = models.FloatField(max_length=100,verbose_name="Долгота")
    longtitude = models.FloatField(max_length=100,verbose_name="Широта")
    photo = models.FileField(upload_to='', blank=True)
    signal = models.CharField(max_length=100, verbose_name="Сигнал светофора",null=True)
    location = models.ForeignKey(TraficLightName,verbose_name="shelfafter", on_delete=models.CASCADE, null=True)
    status = models.BooleanField(verbose_name="Айди устройства", null=True)
    class Meta:
        verbose_name = "Светофор"
        verbose_name_plural = "Список светофоров"
    def str(self):
        return f"{self.gradus} - {self.latitude} {self.longtitude} "

class DateOfAccelerometer(models.Model):
    traffic = models.ForeignKey(TrafficLight,verbose_name="shelfafter", on_delete=models.CASCADE, null=True)
    x = models.CharField(max_length=100, verbose_name="x", default='0')
    y = models.CharField(max_length=100,verbose_name="y",null=True)
    z = models.CharField(max_length=100,verbose_name="z",null=True)

class Devices(models.Model):
    user = models.ForeignKey(User,verbose_name="Пользователь", on_delete=models.CASCADE, null=True)
    device = models.CharField(max_length=100,verbose_name="Устройство", null=True)

class UserRoles(models.Model):
    id_user =models.ForeignKey(User,verbose_name="Id пользователя", on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(verbose_name="Роль администратора", null=True)
    is_information_collector =models.BooleanField(verbose_name="Роль сборщика информации", null=True)
    is_handler  = models.BooleanField(verbose_name="Роль обработчика", null=True)
