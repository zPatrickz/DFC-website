from django.test import TestCase

# Create your tests here.
from core.models import *

class PostMethodTests(TestCase):

    def setUp(self):
        User.objects.create()
        Organization.objects.create()
        Activity.create(name = "a1", organizations = Organization.objects.all())
        Post.create(title = "po1", content = "content",author = User.objects.get(id = 1), organization = Organization.objects.get(id = 1), activity = Activity.objects.get(name = "a1"))

    def test_update_title(self):
        p1 = Post.objects.get(title = "po1")
        p1.update_title("Post1")
        self.assertEqual(p1.title,"Post1")

    def test_update_content(self):
        p1 = Post.objects.get(title = "po1")
        p1.update_content("Hahah")
        self.assertEqual(p1.content,"Hahah")
        
class ActivityMethodTests(TestCase):
    
    def setUp(self):
        User.objects.create()
        Organization.objects.create()
        Organization.objects.create()
        Place.create("p1",1.0,1.0)
        Place.create("p2",2.0,2.0)
        Activity.create(name = "a1", organizations = Organization.objects.all())
        Post.create(title = "po1", content = "content",author = User.objects.get(id = 1), organization = Organization.objects.get(id = 1), activity = Activity.objects.get(name = "a1"))
        
    def test_update_information(self):
        a1 = Activity.objects.get(name="a1")
        
        original_name = a1.name
        a1.update_name("")
        self.assertEqual(a1.name,original_name)
        a1.update_name("activity1")
        self.assertEqual(a1.name,"activity1")
        
        original_desc = a1.desc
        a1.update_desc("")
        self.assertEqual(a1.desc,original_desc)
        a1.update_desc("Blahblah")
        self.assertEqual(a1.desc,"Blahblah")
        
        original_official_link = a1.official_link
        a1.update_official_link("")
        self.assertEqual(a1.official_link,original_official_link)
        a1.update_official_link("http://link")
        self.assertEqual(a1.official_link,"http://link")
        
    def test_place_methods(self):
        a1 = Activity.objects.get(name="a1")
        p1 = Place.objects.get(name="p1")
        p2 = Place.objects.get(name="p2")
        
        a1.add_place(p1)
        a1.add_place(p2)
        self.assertEqual(list(a1.places.all()),[p1,p2])
        
        a1.remove_place(p1)
        self.assertEqual(list(a1.places.all()),[p2])
        
    def test_status_change_methods(self):
        a1 = Activity.objects.get(name="a1")
        
        self.assertEqual(a1.status,'PRP')
        
        a1.publish()
        self.assertEqual(a1.status,'ONG')
        
        a1.cancel()
        self.assertEqual(a1.status,'ABD')
        
        a1.lock()
        self.assertEqual(a1.status,'FRZ')
        
        a1.finish()
        self.assertEqual(a1.status,'FIN')
    
        