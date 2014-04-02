import os
from django.conf import settings

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
        {'theme': "modern", 'relative_urls': False})

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = False#getattr(settings, 'TINYMCE_FILEBROWSER',
        #'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL',os.path.join(settings.STATIC_URL, 'tinymce/tinymce.min.js'))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT',os.path.join(settings.STATIC_ROOT, 'tinymce'))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL','%sjs/tinymce/tinymce.js' % settings.MEDIA_URL)
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tinymce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
