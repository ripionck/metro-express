from django.db import models
from django.contrib.auth.models import User
from train.models import Train, Station
from . constants import SEAT_CLASS_TYPES

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='bookings')
    class_type = models.CharField(max_length=50, choices=SEAT_CLASS_TYPES, null=True, blank=True)
    seats_booked = models.IntegerField()
    selected_seat = models.CharField(max_length=100, null=True, blank=True)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='from_station', null=True, blank=True)
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE,                 related_name='to_station', null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Passenger: {self.user.first_name} {self.user.last_name} , Train: {self.train.name}, Total seats: {self.seats_booked}, Class: {self.class_type}, From: {self.from_station}, To: {self.to_station}'