from django.conf.urls import patterns, url
from accounts import views as accounts_views

urlpatterns = patterns('', 
	url(r'login/$', accounts_views.login, name='login'), 
	url(r'logout/$', accounts_views.logout, name='logout'), 
	url(r'organization/signup/$', accounts_views.signup_organization, name='signup_organization'), 
	url(r'register/$', accounts_views.register, name='register'), 
	url(r'profile/$', accounts_views.user_profile, name='profile'),
)