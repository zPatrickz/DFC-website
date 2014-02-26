from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from views import register, user_profile

urlpatterns = patterns('',
                       url(r'login/$', login),
                       url(r'logout/$', logout, {'next_page': '/index'}),
                       url(r'register/$', register),
                       url(r'profile/$', user_profile),
                       )