from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from activity import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'activity_home'),
    url(r'^new/', views.new_activity, name = 'activity_new'),
)