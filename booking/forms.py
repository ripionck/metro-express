# forms.py
from django import forms
from .models import Booking, SEAT_CLASS_TYPES
from train.models import Station

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['class_type', 'seats_booked', 'selected_seat', 'from_station', 'to_station']

    class_type = forms.ChoiceField(choices=SEAT_CLASS_TYPES, required=False)
    from_station = forms.ModelChoiceField(queryset=Station.objects.all(), required=False)
    to_station = forms.ModelChoiceField(queryset=Station.objects.all(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        from_station = cleaned_data.get('from_station')
        to_station = cleaned_data.get('to_station')

        if from_station and to_station and from_station == to_station:
            raise forms.ValidationError("From station and To station should be different.")

        return cleaned_data
