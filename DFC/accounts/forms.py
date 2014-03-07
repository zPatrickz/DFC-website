# -*- coding: utf-8 -*-
from django import forms
from core.models import Organization
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton


class OrganizationSignUpForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(OrganizationSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'Join Volunteer Organization',
                'name',
                'email',
                'password',
                StrictButton('Sign Up', value='Create', css_class='btn btn-default col-sm-offset-2'),
            ),
        )

    class Meta:
        model = Organization
