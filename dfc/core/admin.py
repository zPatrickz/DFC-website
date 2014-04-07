from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from core.models import *
from accounts.forms import UserCreationForm, UserChangeForm, OrganizationCreationForm

admin.site.unregister(Group)


class MembershipInline(admin.TabularInline):
	model = Membership
	extra = 1


class EmailUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
		(_('Profile'), {'fields': ('birthday', 'telephone', 'credit', 'qq', 'descriptions')}), 
		(_('Permissions'), {'fields': ('is_active', 'is_staff')}),
		(_('Important date'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide', ),
			'fields': ('first_name', 'last_name', 'email', 'password', 'password2')
		}),
	)

	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('email', 'is_staff', 'is_active')
	list_filter = ('is_staff', 'is_active')
	search_fields = ('email', )
	ordering = ('email', )
	filter_horizontal = ()
	

class OrganizationAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}), 
		(_('Profile'), {'fields': ('birthday', 'telephone', 'credit', 'descriptions')}), 
		(_('Permissions'), {'fields': ('is_active', 'is_staff')}), 
		(_('Important date'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide', ),
			'fields': ('username', 'email', 'password', 'password2')
		}),
	)
	inlines = (MembershipInline, )
	add_form = OrganizationCreationForm

	list_display = ('email', 'username', 'is_staff', 'is_active')
	list_filter = ('is_staff', 'is_active')
	search_fields = ('email', 'username')
	ordering = ('email', 'username')
	filter_horizontal = ()


# Register your models here.
admin.site.register(User, EmailUserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Place)
admin.site.register(ActivityPost)
admin.site.register(Activity)
admin.site.register(Participation)
admin.site.register(Membership)
