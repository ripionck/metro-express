from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    balance_after_transaction = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} {self.amount}'