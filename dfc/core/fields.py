from django.forms import ModelChoiceField
from django.db.models.fields import Field,CharField
from django.db.models.fields.related import ForeignKey,ManyToOneRel
from core.widgets import PhotoWidget, SimpleEditorTitleWidget,SimpleEditorContentWidget
from photologue.models import Photo,Gallery
from south.modelsinspector import add_introspection_rules

class ImagePickerField(ModelChoiceField):
    def __init__(self, *args, **kwargs):
        category = kwargs.pop('category')
        self.widget = PhotoWidget(attrs={'category':category})
        super(ImagePickerField, self).__init__(*args, **kwargs)

class PhotoField(ForeignKey):
    # parameter category - tell the field how this photo will be displayed
    #                       may be one of the following:
    #                       photo : a standard photo
    #                       activity_cover : cover of an activity
    #                       that's all for now
     
    def __init__(self,category='photo',to=None,**kwargs):
        self.category = category
        super(PhotoField,self).__init__(Photo,None,ManyToOneRel,**kwargs)
        
    def formfield(self, **kwargs):
        kwargs.update({"category":self.category,'form_class': ImagePickerField})
        return super(PhotoField, self).formfield(**kwargs)
        
    def validate(self, value, model_instance):
        # TODO: restrict the field value within range of category
        super(PhotoField, self).validate(value, model_instance)
        '''if self.rel.parent_link:
            return
        super(ForeignKey, self).validate(value, model_instance)
        if value is None:
            return

        using = router.db_for_read(model_instance.__class__, instance=model_instance)
        qs = self.rel.to._default_manager.using(using).filter(
                **{self.rel.field_name: value}
             )
        qs = qs.complex_filter(self.rel.limit_choices_to)
        if not qs.exists():
            raise exceptions.ValidationError(
                self.error_messages['invalid'],
                code='invalid',
                params={'model': self.rel.to._meta.verbose_name, 'pk': value},
            )'''
            
        
try:
    add_introspection_rules([], ["^core\.fields\.PhotoField"])
    add_introspection_rules([], ["^core\.fields\.SimpleEditorTitleField"])
    add_introspection_rules([], ["^core\.fields\.SimpleEditorContentField"])
except:
    pass