# -*- coding: utf-8 -*-
from django import forms
from models import UserProfile
from core.models import Organization
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton
from django.forms.extras.widgets import SelectDateWidget


GENDER = (
    ('M', '男'),
    ('F', '女'),
    ('A', '女博士'),
)


class UserProfileForm(forms.ModelForm):
    #按照这个模式来设定样式
    true_name = forms.CharField(max_length=20, required=False)
    gender = forms.ChoiceField(required=False, choices=GENDER)
    college = forms.CharField(max_length=40, required=False,
                              widget=forms.TextInput(attrs={'placeholder': '学校', 'class': 'input-xlarge'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'input-xlarge'}))
    phone = forms.CharField(max_length=11, required=False)
    qq = forms.CharField(max_length=11, required=False)
    description = forms.CharField(max_length=140, required=False, widget=forms.Textarea)

    class Meta:
        model = UserProfile
        exclude = ['user',]

class OrganizationForm(forms.ModelForm):

    name = forms.CharField(max_length = 256)
    official_link = forms.CharField(max_length = 1024)

    def __init__(self, *args, **kwargs):
        super(OrganizationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'organization signup',
                'name',
                'official_link',
                StrictButton('submit', value='Create', css_class='btn btn-default col-sm-offset-2'),
            ),
        )

    class Meta:
        model = Organization
        exclude = ('memebers', )
