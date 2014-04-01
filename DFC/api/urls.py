from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from api import views

urlpatterns = patterns('',
    url(r'^gallery/list', views.gallery_list, name = 'api_gallery_list'),
    url(r'^gallery/(?P<gal_id>\d+)/list', views.gallery_photo_list, name = 'api_gallery_photo_list'),
)
