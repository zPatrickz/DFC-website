from django.db import models
from filer.models import File
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
import os

class Document(File):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    belong_to = generic.GenericForeignKey('content_type', 'object_id')
    visit = models.PositiveIntegerField(default=0)
    
    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        # the extensions we'll recognise for this file type
        filename_extensions = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf']
        for ext in filename_extensions:
            if iname.endswith(ext):
                return True
        return False
        
    def clean(self):
        super(Document,self).clean()
        if not self.__class__.matches_file_type(self.file.name,None,None):
            raise ValidationError('Document type not support')
                
    @property
    def display_url(self):
        if self.content_type == ContentType.objects.get(app_label='core',model='activity'):
            return reverse("activity_detail_doc_detail", args=(self.object_id,self.id))
            
    class Meta:
        app_label = 'document'
        