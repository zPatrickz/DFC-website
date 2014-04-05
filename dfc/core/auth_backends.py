from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model

class UserModelBackend(ModelBackend):
	def authenticate(self, email=None, password=None):
		try:
			user = self.abstract_user_class.objects.get(email=email)
			if user.check_password(password):
				return self.inherited_user_class(user).objects.get(email=email)
		except self.abstract_user_class.DoesNotExist:
			return None
			
	def get_user(self, user_id):
		try:
			user = self.abstract_user_class.objects.get(pk=user_id)
			return self.inherited_user_class(user).objects.get(email=user.email)
		except self.abstract_user_class.DoesNotExist:
			return None
	
	@property
	def abstract_user_class(self):
		if not hasattr(self, '_user_class'):
			self._user_class = get_model(*settings.AUTH_USER_MODEL.split('.', 2))
			if not self._user_class:
				raise ImproperlyConfigured('Could not get authe user model')
		return self._user_class
	
	def inherited_user_class(self, user):
		if user.is_superuser:
			self._user_class = get_model('core', 'BaseEmailUser')	
		elif user.is_organization:
			self._user_class = get_model('core', 'Organization')
		else:
			self._user_class = get_model('core', 'User')
		if not self._user_class:
			raise ImproperlyConfigured('Could not get auth user model')
		return self._user_class

