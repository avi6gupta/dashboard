from django import forms
from django.forms.widgets import Cale

class EntryForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateField(widget=DateInput())
    description = forms.CharField(widget=forms.Textarea)
    start_time = forms.TimeField()
    end_time = forms.TimeField()

