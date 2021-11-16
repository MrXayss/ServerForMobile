from datetime import datetime
from django.db import models


class InfoTrafficLight(models.Model):
    gradus = models.FloatField(max_length=100,verbose_name="Градусы")
    latitude = models.FloatField(max_length=100,verbose_name="Долгота")
    longtitude = models.FloatField(max_length=100,verbose_name="Широта")
    class Meta:
        verbose_name = "Светофор"
        verbose_name_plural = "Список светофоров"
    def str(self):
        return f"{self.gradus} - {self.latitude} {self.longtitude} "