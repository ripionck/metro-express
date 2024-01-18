from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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
    
class ProfileUpdateForm(forms.ModelForm):
    nid_no = forms.CharField(max_length=10)
    mobile_no = forms.CharField(max_length=12)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    house_no = forms.IntegerField()
    road_no = forms.CharField(max_length=50)
    zip_code = forms.IntegerField()
    city = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            try:
                # Use .first() to get a single instance
                passenger = self.instance.passenger.first()
            except Passenger.DoesNotExist:
                passenger = None

        if passenger:
            self.fields['gender'].initial = passenger.gender
            self.fields['nid_no'].initial = passenger.nid_no
            self.fields['mobile_no'].initial = passenger.mobile_no
            self.fields['date_of_birth'].initial = passenger.date_of_birth
            self.fields['road_no'].initial = passenger.road_no
            self.fields['house_no'].initial = passenger.house_no
            self.fields['zip_code'].initial = passenger.zip_code
            self.fields['city'].initial = passenger.city

    def save(self, commit=True):
        passenger = super().save(commit=False)
        if commit:
            passenger.save()

            # Retrieve or create passenger instance
            passenger, created = Passenger.objects.get_or_create(user=passenger)

            # Update fields based on form data
            passenger.date_of_birth = self.cleaned_data['date_of_birth']
            passenger.gender = self.cleaned_data['gender']
            passenger.nid_no = self.cleaned_data['nid_no']
            passenger.mobile_no = self.cleaned_data['mobile_no']
            passenger.road_no = self.cleaned_data['road_no']
            passenger.house_no = self.cleaned_data['house_no']
            passenger.zip_code = self.cleaned_data['zip_code']
            passenger.city = self.cleaned_data['city']

            passenger.save()

        return passenger


class PasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Confirm new password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User 
        fields = ('old_password', 'new_password1', 'new_password2')