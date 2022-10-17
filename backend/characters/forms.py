from django import forms
from django import forms

from .models import *

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['season_no', 'start_yr', 'end_yr']