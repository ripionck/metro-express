from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    comment = forms.Textarea(
        label='Comment',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Review
        fields = ['comment']