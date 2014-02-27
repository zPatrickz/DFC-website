from django.db import models

# Core classes for DFC Project

# For general field usage, please refer to https://docs.djangoproject.com/en/1.6/ref/models/fields/
# For ManyToManyField usage, please refer to https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/
# and
# https://docs.djangoproject.com/en/1.6/topics/db/models/#intermediary-manytomany


class User(models.Model):
    GENDER_CHOICES = (
        ('MA','Male'),
        ('FM','Female'),
    )
    name        = models.CharField(max_length = 256)
    email       = models.EmailField(max_length = 254, unique = True)
    nickname    = models.CharField(max_length = 256)
    password    = models.CharField(max_length = 256)
    birthday    = models.DateField(null = True)
    gender      = models.CharField(max_length = 2,choices = GENDER_CHOICES)
    mobile      = models.CharField(max_length = 32)
    qq          = models.BigIntegerField(null = True)
    avatar      = models.CharField(max_length = 1024)#change to ImageField after MEDIA_ROOT in settings.py is specified
    desc        = models.TextField(null = True)
    create_time = models.DateTimeField(auto_now_add = True)
    last_login  = models.DateTimeField()
    
class Organization(models.Model):
    name            = models.CharField(max_length = 256, unique = True)
    members         = models.ManyToManyField(User, through = "Membership")
    official_link   = models.CharField(max_length = 1024)
    
class Place(models.Model):
    name        = models.CharField(max_length = 256)
    longitude   = models.FloatField()
    latitude    = models.FloatField()
    class Meta:
        unique_together = (("longitude", "latitude"),)

class Post(models.Model):
    '''Forum Posts'''
    pass
    
class Poster(models.Model):
    pass
    

class Activity(models.Model):
    STATUS_CHOICES = (
        ('DFT','Draft'),
        ('ONG','Ongoing'),
        ('ABD','Abandoned'),
        ('FRZ','Frozen'),
        ('FIN','Finished'),
    )
    name = models.CharField(max_length = 256)
    organization = models.ManyToManyField(Organization)
    participants = models.ManyToManyField(User, through = "Participation")
    place = models.ForeignKey(Place)
    desc = models.TextField()
    keywords = models.TextField()
    config = models.CharField(max_length = 1024)
    cover = models.CharField(max_length = 1024)#change to ImageField after MEDIA_ROOT in settings.py is specified
    posts = models.ManyToManyField(Post)
    posters = models.ManyToManyField(Poster)
    official_link = models.CharField(max_length = 1024)
    create_time = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 3, choices = STATUS_CHOICES)
    start_time = models.DateTimeField(null = True)
    end_time = models.DateTimeField(null = True)
    visits = models.PositiveIntegerField(default = 0)
    def setConfig(name,value):
        '''control the values in config string'''
        pass
    def getConfig(name):
        '''get the values in config string'''
        pass
    class Meta:
        pass
        #unique_together = (("name","organization"))
        ##The reason not to use unique_together here and in other models:https://code.djangoproject.com/ticket/702


class Participation(models.Model):
    '''Participation describes the relationship between users and activities'''
    ROLE_CHOICES = (
        ('ORG','Organizer'),
        ('MEM','Member'),
    )
    STAGE_CHOICES = (
        ('FLW','Follow'),
        ('APL','Apply'),
        ('ATD','Attended'),
    )
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    role = models.CharField(max_length = 3, choices = ROLE_CHOICES)
    stage = models.CharField(max_length = 3, choices = STAGE_CHOICES)
    class Meta:
        unique_together = (("user","activity"))
        
class Membership(models.Model):
    '''Membership describes the relationship between users and organizations'''
    ROLE_CHOICES = (
        ('FND','Founder'),
        ('MGR','Manager'),
        ('MEM','Member'),
    )
    user = models.ForeignKey(User)
    organization = models.ForeignKey(Organization)
    role = models.CharField(max_length = 3,choices = ROLE_CHOICES)
    join_time = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = (("user","organization"))
    