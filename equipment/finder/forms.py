from django.forms import ModelForm
from .models import Finder
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'



class SearchForm(ModelForm):
    class Meta:
        model = Finder
        fields = "__all__"
        widgets = {
            'date': DateInput
            }