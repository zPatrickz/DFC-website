# -*- coding: utf-8 -*-
from django import forms
from models import UserProfile
from core.models import Organization
from crispy_forms.helper import FormHelper
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
    # members = models.ModelMultipleChoiceField()
    official_link = forms.CharField(max_length = 1024)

    helper = FormHelper()
    helper.form_class = 'form_horizatal'
    helper.form_id = 'id_organization_form'
    helper.form_method = 'post'
    helper.form_action = 'submit_organization_form'
    # helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Organization
        exclude = ('memebers', )

        