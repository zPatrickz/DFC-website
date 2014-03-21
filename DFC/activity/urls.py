from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from activity import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'activity_home'),
    url(r'^new/', views.add_or_update_activity, name = 'activity_new'),
    url(r'^update/(?P<act_id>\d+)', views.add_or_update_activity, name = 'activity_update'),
)
