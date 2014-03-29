from django.db.models.fields.related import ForeignKey,ManyToOneRel
from photologue.models import Photo,Gallery
from south.modelsinspector import add_introspection_rules

class PhotoField(ForeignKey):
    def __init__(self,to=None,**kwargs):
        super(PhotoField,self).__init__(Photo,None,ManyToOneRel,**kwargs)

try:
    add_introspection_rules([], ["^core\.fields\.PhotoField"])
except:
    pass