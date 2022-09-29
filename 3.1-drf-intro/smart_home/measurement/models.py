from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    screenshot = models.ImageField(null=True, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    def __str__(self):
        return self.temperature
