from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import *

admin.site.unregister(Group)

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Place)
admin.site.register(Post)
admin.site.register(Activity)
admin.site.register(Participation)
admin.site.register(Membership)
