from django import forms
from core.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton
from django.forms.extras.widgets import SelectDateWidget

class ActivityForm(forms.ModelForm):
    
    class Meta:
        model = Activity
        fields = ['name','desc','cover','official_link','start_time','end_time']