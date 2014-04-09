import markdown
from markdown.inlinepatterns import Pattern
from photologue.models import Photo
AUTOLINK_RE = r'(?<!"|>)((https?://|www)[-\w./#?%=&]+)'
PHOTO_RE = r'(\{photo )(\d+)\}'
#DOC_RE = r'(\[photo )(d+)\]'

class PhotoTagPattern(Pattern):
    """
    Return element of type `tag` with a text attribute of group(3) 
    of a Pattern and with the html attributes defined with the constructor.

    """
    def __init__ (self, pattern):
        Pattern.__init__(self, pattern)

    def handleMatch(self, m):
        el = markdown.util.etree.Element('img')
        try:
            photo = Photo.objects.get(id=m.group(3))
        except Photo.DoesNotExist:
            return el
        el.set("src",photo.get_url("photo","large"))
        return el
        
class AutoLinkPattern(Pattern):

    def handleMatch(self, m):
        el = markdown.util.etree.Element('a')
        if m.group(2).startswith('http'):
            href = m.group(2)
        else:
            href = 'http://%s' % m.group(2)
        el.set('href', href)
        el.text = m.group(2)
        return el

class SimpleEditorSyntaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        photo_tag = PhotoTagPattern(PHOTO_RE)
        md.inlinePatterns.add('autolink', 
                    AutoLinkPattern(AUTOLINK_RE, self), '_begin')
        md.inlinePatterns.add('photo', photo_tag, '<autolink')
        

def makeExtension(configs=None):
    return SimpleEditorSyntaxExtension(configs=configs)