from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from document import views

urlpatterns = patterns('',
#	url(r'^$', views.index, name = 'document_home'),
    url(r'^new/', views.new, name = 'doc_new'),
    url(r'^(?P<doc_id>\d+)/',views.detail, name = 'doc_detail'),
)
