from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE


# Create your models here.
class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger')
    nid_no = models.CharField(max_length=10, unique=True)
    mobile_no = models.CharField(max_length = 12, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER_TYPE, max_length=20)
    house_no = models.IntegerField()
    road_no = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=20)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
