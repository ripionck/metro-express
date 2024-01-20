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
            ('Economy', 'Economy'),
            ('FirstClass', 'First Class'),
            ('Business', 'Business'),
            ('Premium', 'Premium'),
            ('Luxury', 'Luxury'),
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
        fields = ['name', 'available_seats', 'day_of_week', 'start_station', 'end_station', 'route_stations']

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

class TrainUpdateForm(ModelForm):
    class Meta:
        model = Train
        fields = ['name', 'available_seats', 'day_of_week', 'start_station', 'end_station', 'route_stations']

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

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['train', 'station', 'arrival_time', 'departure_time', 'halt_duration_minutes']

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
                
class ScheduleUpdateForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['train', 'station', 'arrival_time', 'departure_time', 'halt_duration_minutes']

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

class TrainReviewForm(ModelForm):
    class Meta:
        model = TrainReview
        fields = ['user', 'train', 'comment']
