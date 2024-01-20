from django import forms
from django.forms import ModelForm
from .models import Station, Day, Train, Schedule, TrainReview

class TrainSearchForm(forms.Form):
    from_station = forms.CharField(label='From', max_length=100)
    to_station = forms.CharField(label='To', max_length=100)
    date = forms.DateField(label='Date')
    travel_class = forms.ChoiceField(
        label='Class',
        choices=[
            ('economy', 'Economy'),
            ('business', 'Business'),
        ]
    )

class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'slug']

class DayForm(ModelForm):
    class Meta:
        model = Day
        fields = ['name']

class TrainForm(ModelForm):
    class Meta:
        model = Train
        fields = "__all__"

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['train', 'station', 'arrival_time', 'departure_time', 'halt_duration_minutes']

class TrainReviewForm(ModelForm):
    class Meta:
        model = TrainReview
        fields = ['user', 'train', 'comment']
