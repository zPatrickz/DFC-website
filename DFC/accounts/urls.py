from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = patterns('',
	url(r'login/$', auth_views.login, name='login'),
	url(r'logout/$', auth_views.logout, {'next_page': '/index'}, name='logout'),
	url(r'register/$', accounts_views.register, name='register'),
	url(r'profile/$', accounts_views.user_profile, name='profile'),
)