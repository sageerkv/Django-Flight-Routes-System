from django import forms
from .models import AirportRouteNode

class AirportRouteNodeForm(forms.ModelForm):
    class Meta:
        model = AirportRouteNode
        fields = ['route_name', 'airport_code', 'position', 'duration']


class NthNodeSearchForm(forms.Form):
    route_name = forms.CharField(max_length=100)
    airport_code = forms.CharField(max_length=10)
    direction = forms.ChoiceField(choices=[('L', 'Left'), ('R', 'Right')])
    n = forms.IntegerField(min_value=1)


class ShortestBetweenForm(forms.Form):
    route_name = forms.CharField(max_length=100)
    start_airport_code = forms.CharField(max_length=10)
    end_airport_code = forms.CharField(max_length=10)
