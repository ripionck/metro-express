from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import PassengerProfile
from .constants import GENDER_TYPE


class PassengerRegistrationForm(UserCreationForm):
    nid_no = forms.CharField(max_length=10)
    mobile_no = forms.CharField(max_length = 12)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 10}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email',
                 'date_of_birth', 'gender', 'nid_no', 'mobile_no', 'address']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already exists.')
        return email
    

    def save(self, commit=True):
    # Save the user instance
        user_instance = super().save(commit=False)
        user_instance.is_active = False  

        if commit:
            user_instance.save()

            # Retrieve additional data from the form
            gender = self.cleaned_data.get('gender')
            nid_no = self.cleaned_data.get('nid_no')
            date_of_birth = self.cleaned_data.get('date_of_birth')
            mobile_no = self.cleaned_data.get('mobile_no')
            address = self.cleaned_data.get('address')

            # Create passenger instance
            PassengerProfile.objects.create(
                user=user_instance,
                gender=gender,
                date_of_birth=date_of_birth,
                nid_no=nid_no,
                mobile_no=mobile_no,
                address = address
            )

        return user_instance
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to form fields for styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
    
class ProfileUpdateForm(forms.ModelForm):
    nid_no = forms.CharField(max_length=10)
    mobile_no = forms.CharField(max_length=12)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to form fields for styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })

        if self.instance:
            try:
                # Use .first() to get a single instance
                passenger = self.instance.passenger.first()
            except PassengerProfile.DoesNotExist:
                passenger = None

        if passenger:
            self.fields['gender'].initial = passenger.gender
            self.fields['nid_no'].initial = passenger.nid_no
            self.fields['mobile_no'].initial = passenger.mobile_no
            self.fields['date_of_birth'].initial = passenger.date_of_birth
            self.fields['address'].initial = passenger.address

    def save(self, commit=True):
        passenger = super().save(commit=False)
        if commit:
            passenger.save()

            # Retrieve or create passenger instance
            passenger, created = PassengerProfile.objects.get_or_create(user=passenger)

            # Update fields based on form data
            passenger.date_of_birth = self.cleaned_data['date_of_birth']
            passenger.gender = self.cleaned_data['gender']
            passenger.nid_no = self.cleaned_data['nid_no']
            passenger.mobile_no = self.cleaned_data['mobile_no']
            passenger.address = self.cleaned_data['address']

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