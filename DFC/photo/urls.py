from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from photo import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'photo_home'),
    
    url(r'^(?P<photo_id>\d+)/', views.view_photo, name = 'photo_view'),
    url(r'^new/(?P<album_id>\d+)/', views.add_photo, name = 'photo_new'),
    url(r'^album/(?P<album_id>\d+)/', views.view_album, name = 'photo_view'),
    url(r'^album/new/', views.add_or_update_album, name = 'album_new'),
    url(r'^album/update/(?P<album_id>\d+)', views.add_or_update_album, name = 'album_update'),
)