#-*- coding: utf-8 -*-
from filer.fields.file import AdminFileWidget, AdminFileFormField, \
    FilerFileField
from filer.models import Document


class DocumentField(FilerFileField):
    default_model_class = Document
