from django import forms
from django.conf import settings
from core.models import *
from core.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton
from django.forms.extras.widgets import SelectDateWidget
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        widgets = {
                    'name': forms.TextInput(),
                    'desc': forms.Textarea(
                        attrs={'placeholder': 'No more than 240 characters'}),
                    'start_time': DateTimeWidget(options = {'format': 'dd/mm/yyyy HH:ii P','autoclose': 'true'}, usel10n = True),
                    'end_time': DateTimeWidget(options = {'format': 'dd/mm/yyyy HH:ii P','autoclose': 'true'}, usel10n = True)
                    }
        exclude = ['status','participants','visits']