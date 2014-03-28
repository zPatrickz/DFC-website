from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from activity import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'activity_home'),
    url(r'^new/(?P<step>\w+)', views.new_or_update_activity, name = 'activity_new'),
    url(r'^new/', views.new_or_update_activity, name = 'activity_new'),
    #url(r'^(?P<act_id>\d+)/settings/', views.new_or_update_activity, name = 'activity_update'),
    url(r'^(?P<act_id>\d+)/album',views.detail_album, name = 'activity_detail_album'),
    url(r'^(?P<act_id>\d+)/detail',views.detail_detail, name = 'activity_detail_detail'),
    url(r'^(?P<act_id>\d+)/discuss',views.detail_discuss, name = 'activity_detail_discuss'),
    url(r'^(?P<act_id>\d+)/doc',views.detail_doc, name = 'activity_detail_doc'),
    url(r'^(?P<act_id>\d+)/notice',views.detail_notice, name = 'activity_detail_notice'),
    url(r'^(?P<act_id>\d+)/post',views.detail_post, name = 'activity_detail_post'),
    url(r'^(?P<act_id>\d+)/',views.detail_post, name = 'activity_detail'),
    
    
)
