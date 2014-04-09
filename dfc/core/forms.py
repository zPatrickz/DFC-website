from django import forms
from core.models import ActivityPost
from simpleeditor.widgets import SimpleEditorTitleWidget,SimpleEditorContentWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field

class ActivityPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(ActivityPostForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Div('title'),
                Div('content'),
                ButtonHolder(
                    Submit('submit', 'Submit', css_class='btn btn-primary')
                )
            )
    class Meta:
        model = ActivityPost
        widgets = {
            "title":SimpleEditorTitleWidget,
            "content":SimpleEditorContentWidget
        }
        fields = ['title','content','activity','author','category']