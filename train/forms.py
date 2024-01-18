from django import forms

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
    