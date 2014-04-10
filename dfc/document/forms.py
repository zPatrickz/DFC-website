from django import forms
from document.models import Document
from simpleeditor.widgets import SimpleEditorTitleWidget,SimpleEditorContentWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field

class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        from django.contrib.contenttypes.models import ContentType
        activity_type_id = ContentType.objects.get(app_label='core',model='activity').id
        self.helper.layout = Layout(
            Div('file'),
            Div('description'),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )
    class Meta:
        model = Document
        '''widgets = {
                    'name': forms.TextInput(),
                    'desc': forms.Textarea(
                        attrs={'placeholder': 'No more than 240 characters'}),
                    'start_time': DateTimeWidget(options = {'format': 'dd/mm/yyyy HH:ii P','autoclose': 'true'}, usel10n = True),
                    'end_time': DateTimeWidget(options = {'format': 'dd/mm/yyyy HH:ii P','autoclose': 'true'}, usel10n = True)
                    }'''
        exclude = ['name','folder','_file_size','sha1','original_filename','owner','is_public','visit']