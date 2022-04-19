from datetime import datetime
from email.policy import default
from django.db import models


class TraficLightName(models.Model):
    name_trafficlight = models.CharField(max_length=100, verbose_name="Название перекрестка", default='0')

class InfoTrafficLight(models.Model):
    id_device = models.CharField(max_length=100, verbose_name="Айди устройства", default='0')
    gradus = models.FloatField(max_length=100,verbose_name="Градусы")
    latitude = models.FloatField(max_length=100,verbose_name="Долгота")
    longtitude = models.FloatField(max_length=100,verbose_name="Широта")
    photo = models.FileField(upload_to='', blank=True)
    json = models.JSONField(null=True)
    signal = models.CharField(max_length=100, verbose_name="Сигнал светофора",null=True)
    location = models.ForeignKey(TraficLightName,verbose_name="shelfafter", on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = "Светофор"
        verbose_name_plural = "Список светофоров"
    def str(self):
        return f"{self.gradus} - {self.latitude} {self.longtitude} "