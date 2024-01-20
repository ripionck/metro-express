from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from train.models import Train, Station
from .constants import SEAT_CLASS_TYPES
from decimal import Decimal

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='bookings')
    class_type = models.CharField(max_length=50, choices=SEAT_CLASS_TYPES)
    seats_quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    selected_seat = models.CharField(max_length=100)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='from_station')
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='to_station')
    booking_date = models.DateTimeField(auto_now_add=True)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_prices(self):
        #Pricing model based on seat_quantity and class_type
        if self.class_type == 'Economy':
            base_price = Decimal('200.00')
        elif self.class_type == 'Business':
            base_price = Decimal('250.00')
        elif self.class_type == 'Premium':
            base_price = Decimal('300.00')
        elif self.class_type == 'Luxury':
            base_price = Decimal('350.00')
        else:
            base_price = Decimal('150.00')  # Default price for other classes

        self.ticket_price = base_price
        self.total_price = base_price * self.seats_quantity

    def save(self, *args, **kwargs):
        if not self.ticket_price or not self.total_price:
            self.calculate_prices()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.train.name} - {self.class_type}'

    class Meta:
        ordering = ['-booking_date']
