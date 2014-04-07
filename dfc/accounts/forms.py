from django import forms
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions
from core.models import Organization, User


class BaseCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """
    error_messages = {
        'duplicate_email': _("A user with that email already exists"),
        'password_mismatch':_("The two password fields didn't match"),
    }
    password = forms.CharField(label=_("Password"), 
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), 
        widget=forms.PasswordInput, 
        help_text=_("Enter the same password as above, for verification")
    )
    def __init__(self, *args, **kwargs):
        super(BaseCreationForm, self).__init__(*args, **kwargs)
        
    class Meta:
        abstract = True
        
    def clean_password2(self):
        password1 = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'], 
                code='password_mismatch'
            )
        return password2
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email'
        )


class UserCreationForm(BaseCreationForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'register'
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'Create your account',
                'first_name', 'last_name', 'email', 'password', 'password2', 
                FormActions(
                    Submit('sign up', _('Sign Up'), css_class='btn col-sm-offset-2'),
                ),
            )
        )

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined', 'credit']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user, but replaces the password field 
    with admin's password has display field.
    """

    password = ReadOnlyPasswordHashField(label=_("Password"), 
        help_text=_("Raw password are not stored, so there is no way to see " 
            "this user's password, but you can change the password using " 
            "<a href=\"password/\">this form</a>"))

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'register'
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'Update your account',
                'first_name', 'last_name', 'descriptions', 'birthday', 'qq', 'telephone',
                FormActions(
                    Submit('sign up', _('Sign Up'), css_class='btn col-sm-offset-2'),
                ),
            )
        )
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]


class OrganizationCreationForm(BaseCreationForm):
    """
    A form for creating a new organization
    """
    
    def __init__(self, *args, **kwargs):
        super(OrganizationCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'register_organization'
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'Join Volunteer Organization',
                'username', 'email', 'password', 'password2', 
                FormActions(
                    Submit('sign up', _('Sign Up'), css_class='btn col-sm-offset-2'),
                )
            ),
        )
    
    class Meta:
        model = Organization
        exclude = ['last_login', 'date_joined', 'credit']
    
    def save(self, commit=True):
        organization = super(OrganizationCreationForm, self).save(commit=False)
        organization.is_organization = True
        organization.set_password(self.cleaned_data["password"])
        if commit:
            organization.save()
        return organization


class OrganizationSettingsForm(forms.ModelForm):
    """
    The Settings Form of organization
    """
    def __init__(self, *args, **kwargs):
        super(OrganizationSettingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-6'
        self.helper.layout = Layout(
            Fieldset(
                '', 
                'username', 'pay_link', 'organization_page', 'birthday', 'descriptions', 
            )
        )
    
    class Meta:
        model = Organization


class SignInForm(forms.Form):
    """
    Sign in form
    """
    email = forms.EmailField(label=_("Email Address"))
    password = forms.CharField(label=_("Password"), max_length=128, 
        widget=forms.PasswordInput())
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(), required=False, 
        label=_("Remember me"))
    
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'login'
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'Sign In', 
                'email', 'password', 'remember_me', 
                FormActions(
                    Submit('sign in', _('Sign In'), css_class='btn col-sm-offset-2'),
                )
            ),
        )
        
    def clean(self):
        """
        Checks for the email and password.
        """
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError(_('Invalid email or password'))
        return self.cleaned_data

