from django.conf.urls import patterns, include, url
from django.contrib import admin
from dfc import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^index/$', views.index, name='index'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
   	url(r'^accounts/', include('accounts.urls')),
)
