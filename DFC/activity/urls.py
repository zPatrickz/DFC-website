from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from activity import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'activity_home'),
    url(r'^new/created/(?P<act_id>\d+)', views.complete_or_view, name = 'activity_complete_or_view'),
    url(r'^new/', views.new, name = 'activity_new'),
    url(r'^(?P<act_id>\d+)/album',views.detail_album, name = 'activity_detail_album'),
    url(r'^(?P<act_id>\d+)/detail',views.detail_detail, name = 'activity_detail_detail'),
    url(r'^(?P<act_id>\d+)/discuss',views.detail_discuss, name = 'activity_detail_discuss'),
    url(r'^(?P<act_id>\d+)/doc',views.detail_doc, name = 'activity_detail_doc'),
    url(r'^(?P<act_id>\d+)/member',views.detail_member, name = 'activity_detail_member'),
    url(r'^(?P<act_id>\d+)/notice',views.detail_notice, name = 'activity_detail_notice'),
    url(r'^(?P<act_id>\d+)/post/new',views.detail_post_new, name = 'activity_detail_post_new'),
    url(r'^(?P<act_id>\d+)/post',views.detail_post, name = 'activity_detail_post'),
    url(r'^(?P<act_id>\d+)/settings/(?P<category>\w*)',views.detail_settings, name = 'activity_detail_settings'),
    url(r'^(?P<act_id>\d+)/',views.detail_post, name = 'activity_detail'),
)
