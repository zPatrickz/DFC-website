from django.db.models.fields.related import ForeignKey
from photologue.models import Photo,Gallery
from south.modelsinspector import add_introspection_rules

class PhotoField(ForeignKey):
    def __init__(self, *args, **kwargs):
        super(PhotoField, self).__init__(Photo)
        
add_introspection_rules([], ["^core\.fields\.PhotoField"])