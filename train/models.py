from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from account.models import PassengerProfile



# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Train(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    available_seats = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    day_of_week = models.ManyToManyField(Day)
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_station', null=True, blank=True)
    end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end_station', null=True, blank=True)
    route_stations = models.ManyToManyField(Station)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Schedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    halt_duration_minutes = models.DurationField()

    def __str__(self):
        return f'{self.train.name}'

    def clean(self):
        if self.arrival_time and self.departure_time and self.arrival_time >= self.departure_time:
            raise ValidationError("Arrival time must be before departure time.")



class TrainReview(models.Model):
    user = models.ForeignKey(PassengerProfile, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.user.first_name} - {self.comment}'