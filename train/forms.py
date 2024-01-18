from django import forms
from .models import Train

class TrainSearchForm(forms.ModelForm):
    from_station = forms.CharField(label='From', max_length=100)
    to_station = forms.CharField(label='To', max_length=100)
    date_of_journey = forms.DateField(label='Date')
    travel_class = forms.ChoiceField(
        label='Class',
        choices=[
            ('economy', 'Economy'),
            ('business', 'Business'),
        ]
    )

    class Meta:
        model = Train
        fields = ['from_station', 'to_station', 'date_of_journey', 'travel_class']

    