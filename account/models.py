from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE


# Create your models here.
class PassengerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger_profile')
    nid_no = models.CharField(max_length=10, unique=True)
    mobile_no = models.CharField(max_length=12, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER_TYPE, max_length=20)
    address = models.TextField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'