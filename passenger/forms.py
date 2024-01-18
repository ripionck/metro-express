from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Passenger
from .constants import GENDER_TYPE

class PassengerRegistrationForm(UserCreationForm):
    nid_no = forms.CharField(max_length=10)
    mobile_no = forms.CharField(max_length = 12)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    house_no = forms.IntegerField()
    road_no = forms.CharField(max_length=50)
    zip_code = forms.IntegerField()
    city = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email',
                 'date_of_birth', 'gender', 'nid_no', 'mobile_no', 'house_no', 'road_no', 'zip_code', 'city']

    def save(self, commit=True):
        # Save the user instance
        passenger = super().save(commit=False)
        if commit:
            passenger.save()
            # Retrieve additional data from the form
            gender = self.cleaned_data.get('gender')
            nid_no = self.cleaned_data.get('nid_no')
            date_of_birth = self.cleaned_data.get('date_of_birth')
            mobile_no = self.cleaned_data.get('mobile_no')
            house_no = self.cleaned_data.get('house_no')
            road_no = self.cleaned_data.get('road_no')
            zip_code = self.cleaned_data.get('zip_code')
            city = self.cleaned_data.get('city')

            # Create passenger instance
            Passenger.objects.create(
                user=passenger,
                gender=gender,
                date_of_birth=date_of_birth,
                nid_no=nid_no,
                mobile_no=mobile_no,
                house_no=house_no,
                road_no = road_no,
                zip_code = zip_code,
                city = city

            )
        return passenger