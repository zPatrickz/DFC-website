from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from views import register, getprofile

urlpatterns = patterns('',
                       url(r'login/$', login),
                       url(r'logout/$', logout),
                       url(r'register/$', register),
                       url(r'profile/$', getprofile),
)
