from django.db import models
from .constants import  DAYS_OF_WEEK


# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    available_seats = models.IntegerField()
    day_of_week = models.CharField(max_length=100, choices=DAYS_OF_WEEK, null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    halt_duration = models.DurationField(null=True, blank=True)
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_station', null=True, blank=True)
    end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end_station', null=True, blank=True)
    route_station = models.ManyToManyField(Station)

    def __str__(self):
        return self.name

