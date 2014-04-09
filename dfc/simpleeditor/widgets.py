from django.forms.widgets import Input
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.forms import forms, widgets

class SimpleEditorTitleWidget(Input):
    def __init__(self, attrs=None):
        super(SimpleEditorTitleWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return format_html('<input type="text" name="'+name+'" value="'+(value if value else "")+'" placeholder="Title Here" class="editor-title" tabindex="0">')
        
class SimpleEditorContentWidget(Input):
    def __init__(self, attrs=None):
        super(SimpleEditorContentWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        from django.template import Context, Template
        from django.template.loader import get_template
        widget_template = get_template('simpleeditor/editor-simple-widget.html')
        html =  widget_template.render(Context({"name":name}))
        return html
        
    def _media(self):
        return widgets.Media(css={'all': ('simpleeditor/editor-simple.css','css/image-picker.css')},
                               js=('js/rangy-core.js','simpleeditor/editor-simple.js','js/image-picker.min.js','js/image-picker-widget.js'))
    media = property(_media)
