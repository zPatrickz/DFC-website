from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = patterns('', 
	url(r'login/$', auth_views.login, {'template_name': 'accounts/login.html',}, name = 'login'), 
	url(r'logout/$', auth_views.logout, {'next_page': '/index'}, name = 'logout'), 
	url(r'organization/signup/$', accounts_views.signup_organization, name = 'signup_organization'), 
	url(r'register/$', accounts_views.register, name = 'register'), 
	url(r'profile/$', accounts_views.user_profile, name = 'profile'),
)