from django.conf.urls import patterns, url
from accounts import views as accounts_views

urlpatterns = patterns('', 
	url(r'login/$', accounts_views.login, name='login'), 
	url(r'logout/$', accounts_views.logout, name='logout'), 
	url(r'organization/register/$', accounts_views.register_organization, name='register_organization'), 
	url(r'register/$', accounts_views.register, name='register'), 
	url(r'profile/$', accounts_views.user_profile, name='profile'), 
	url(r'messages/$', accounts_views.user_message, name='messages'), 
)