from core.models import *

User.objects.create()
Organization.objects.create()
Activity.create(name = "a1", organizations = Organization.objects.all())
Post.create(title = "po1", content = "content",author = User.objects.get(id__exact = 1), organization = Organization.objects.get(id = 1), activity = Activity.objects.get(id =1))
