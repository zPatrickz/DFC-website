# -*- coding: utf-8 -*-
import markdown
from markdown.inlinepatterns import Pattern
from photologue.models import Photo
from document.models import Document

AUTOLINK_RE = r'(?<!"|>)((https?://|www)[-\w./#?%=&]+)'
PHOTO_RE = r'(\{photo )(\d+)\}'
DOC_RE = r'(\{doc )(\d+)\}'

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
        
class DocumentTagPattern(Pattern):
    """
    Return element of type `tag` with a text attribute of group(3) 
    of a Pattern and with the html attributes defined with the constructor.

    """
    def __init__ (self, pattern):
        Pattern.__init__(self, pattern)

    def handleMatch(self, m):
        el = markdown.util.etree.Element('a')
        try:
            doc = Document.objects.get(id=m.group(3))
        except Document.DoesNotExist:
            return el
        el.set("href",doc.display_url)
        el.text = '['+doc.original_filename+']'
        return el

class SimpleEditorSyntaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        
        md.inlinePatterns.add('autolink', 
                    AutoLinkPattern(AUTOLINK_RE, self), '_begin')
        
        photo_tag = PhotoTagPattern(PHOTO_RE)
        md.inlinePatterns.add('photo', photo_tag, '<autolink')
        doc_tag = DocumentTagPattern(DOC_RE)
        md.inlinePatterns.add('doc', doc_tag, '<photo')
        

def makeExtension(configs=None):
    return SimpleEditorSyntaxExtension(configs=configs)