from django import forms
from django.forms.widgets import TextInput
from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control js-mapbox-input-location-field'}),
        }
        labels = {'location': ''}
        