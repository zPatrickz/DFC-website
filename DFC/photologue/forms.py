from django import forms
from django.conf import settings
from photologue.models import Photo,Gallery
from core.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import StrictButton

class PhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'image',
                'title',
                'caption',
                'is_public',
                'tags',
                'crop_from',
                'effect',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )
        super(PhotoForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Photo
        exclude = ['title_slug','date_added']

class GalleryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Create Gallery',
                'title',
                'description',
                'is_public',
                'photos',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )
        super(GalleryForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Gallery
        exclude = ['title_slug','date_added']