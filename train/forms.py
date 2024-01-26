from django import forms
from django.forms import ModelForm
from .models import Train, Schedule

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
    
    arrival_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'], 
    )
    departure_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'], 
    )

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

