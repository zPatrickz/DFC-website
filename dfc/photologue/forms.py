from django import forms
from django.conf import settings
from photologue.models import Photo,Gallery
from core.widgets import DateTimeWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,HTML
from crispy_forms.bootstrap import StrictButton

class PhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        from django.core.urlresolvers import reverse
        self.helper.layout = Layout(
            'image',
            'title',
            'caption',
            'is_public',
            'tags',
            'crop_from',
            'effect',
            'gallery',
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary'),
                HTML('<a href="'+reverse('add-gallery')+'" target="_blank" class="btn btn-primary">Create a Gallery</a>')
            ),
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