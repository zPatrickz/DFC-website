from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^index$', index),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
   	url(r'^accounts/', include('accounts.urls')),
)
