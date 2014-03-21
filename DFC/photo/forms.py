from django import forms
from django.conf import settings
from core.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton
from django.forms.extras.widgets import SelectDateWidget

class JcropWidget(forms.Widget):
  class Media:
    # form media, i.e. CSS and JavaScript needed for Jcrop.
    # You'll have to adopt these to your project's paths.
    css = {
      'all': (settings.STATIC_ROOT + "css/jquery.Jcrop.min.css",)
    }
    js = (
      settings.STATIC_ROOT + "js/jquery.Jcrop.min.js",
    )
  
  # fixed Jcrop options; to pass options to Jcrop, use the jcrop_options
  # argument passed to the JcropForm constructor. See example above.
  jcrop_options = {
                    "onSelect": "storeCoords", 
                    "onChange": "storeCoords",
                  }
  
  # HTML template for the widget. 
  #
  # The widget is constructed from the following parts:
  #
  #  * HTML <img> - the actual image used for displaying and cropping
  #  * HTML <label> and <input type="file> - used for uploading a new
  #                                          image
  #  * HTML <input type="hidden"> - to remember image path and filename
  #  * JS code - The JS code makes the image a Jcrop widget and 
  #              registers an event handler for the <input type="file"> 
  #              widget. The event handler submits the form so the new
  #              image is sent to the server without the user having
  #              to press the submit button.
  # 
  markup = """
  <img id="jcrop-img" src="%(MEDIA_URL)s%(img_fn)s"/><br/>
  <label for="new-img-file">Neues Bild hochladen:</label>
  <input type="file" name="%(UPLOAD_IMG_ID)s" id="%(UPLOAD_IMG_ID)s"/>
  <input type="hidden" name="imagefile" id="imagefile" value="%(imagefile)s"/>
  <script type="text/javascript">
  function storeCoords(c)
  {
    jQuery('#id_x1').val(c.x);
    jQuery('#id_x2').val(c.x2);
    jQuery('#id_y1').val(c.y);
    jQuery('#id_y2').val(c.y2);
  }
  jQuery(function() {
      jQuery('#jcrop-img').Jcrop(%(jcrop_options)s);
      jQuery('#%(UPLOAD_IMG_ID)s').change(function(e){
        var form = jQuery('#%(UPLOAD_IMG_ID)s').parents('form:first');
        form.submit();
      });
  });</script>
    """

  def __init__(self, attrs=None):
    """
    __init__ does nothing special for now
    """
    super(JcropWidget, self).__init__(attrs)
    
  def add_jcrop_options(self, options):
    """
    add jcrop options; options is expected to be a dictionary of name/value
    pairs that Jcrop understands; 
    see http://deepliquid.com/content/Jcrop_Manual.html#Setting_Options
    """
    for k, v in options.items():
      self.jcrop_options[k] = v
    
  def render(self, name, value, attrs=None):
    """
    render the Jcrop widget in HTML
    """
    # translate jcrop_options dictionary to JavaScipt
    jcrop_options = "{";
    for k, v in self.jcrop_options.items():
      jcrop_options = jcrop_options + "%s: %s," % (k, v)
    jcrop_options = jcrop_options + "}"
    
    # fill in HTML markup string with actual data
    output = self.markup % {
                             "MEDIA_URL": settings.MEDIA_URL, 
                             "img_fn": str(value),
                             "UPLOAD_IMG_ID": UPLOAD_IMG_ID,
                             "jcrop_options": jcrop_options,
                             "imagefile": value,
                           }
    return mark_safe(output)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title','desc')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo','desc','album')
