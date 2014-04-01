from django.forms import ModelChoiceField
from django.db.models.fields.related import ForeignKey,ManyToOneRel
from core.widgets import PhotoWidget
from photologue.models import Photo,Gallery
from south.modelsinspector import add_introspection_rules

class ImagePickerField(ModelChoiceField):
    widget = PhotoWidget
    #def __init__(self, *args, **kwargs):
    #    super(ImagePickerField, self).__init__(*args, **kwargs)

class PhotoField(ForeignKey):
    def __init__(self,to=None,**kwargs):
        super(PhotoField,self).__init__(Photo,None,ManyToOneRel,**kwargs)
    def formfield(self, **kwargs):
        new_form_class = {}
        new_form_class.update(kwargs)
        new_form_class.update({'form_class': ImagePickerField})
        return super(PhotoField, self).formfield(**new_form_class)

try:
    add_introspection_rules([], ["^core\.fields\.PhotoField"])
except:
    pass