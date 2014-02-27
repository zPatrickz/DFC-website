from django.contrib import admin
from core.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Place)
admin.site.register(Post)
admin.site.register(Poster)
admin.site.register(Activity)
admin.site.register(Participation)
admin.site.register(Membership)