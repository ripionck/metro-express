from django import forms
from .models import Passenger

class PassengerCreationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'