from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from dfc import views
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^index/$', views.index, name='index'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
   	url(r'^accounts/', include('accounts.urls')),
    url(r'^activity/', include('activity.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^photo/', include('photologue.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ) #comment this when DEBUG=FALSE
