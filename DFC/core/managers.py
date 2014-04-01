from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class EmailUserManager(BaseUserManager):

	def _create_user(self, email, password, is_staff, is_organization, is_superuser, **extra_fields):
		"""
		Creates and saves a User with the given email and password
		"""
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		is_active = extra_fields.pop("is_active", True)
		
		user = self.model(email=email, is_staff=is_staff, 
			is_active=is_active, is_organization=is_organization, is_superuser=is_superuser, 
			last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		is_staff = extra_fields.pop("is_staff", False)
		is_organization = extra_fields.pop("is_organization", False)
		return self._create_user(email, password, is_staff, is_organization, False, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		return self._create_user(email, password, True, False, True, **extra_fields)


class EmailOrganizationManager(EmailUserManager):
	
	def create_user(self, email, password=None, **extra_fields):
		is_staff = extra_fields.pop("is_staff", False)
		return self._create_user(email, password, is_staff, True, False, **extra_fields)

