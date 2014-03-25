from django import forms
from django.conf import settings
from core.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton
from django.forms.extras.widgets import SelectDateWidget
class ActivityForm(forms.ModelForm):
    #jcrop_cover = forms.Field(widget=JcropWidget(), label="", required=False)
    class Meta:
        model = Activity
        fields = ('name','desc','official_link','start_time','end_time')

