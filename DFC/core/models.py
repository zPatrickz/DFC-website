from django.db import models

# Core classes for DFC Project

# For general field usage, please refer to https://docs.djangoproject.com/en/1.6/ref/models/fields/
# For ManyToManyField usage, please refer to https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/
# and
# https://docs.djangoproject.com/en/1.6/topics/db/models/#intermediary-manytomany
# For model instance usage, please refer to https://docs.djangoproject.com/en/1.6/ref/models/instances/#model-instance-methods

class User(models.Model):
    pass
    
class Organization(models.Model):
    pass
    
class Place(models.Model):
    name        = models.CharField(max_length = 256, blank = False)
    longitude   = models.FloatField()
    latitude    = models.FloatField()
    @classmethod
    def create(cls,name,longitude,latitude):
        '''
        Create a place.
        
        Parameters
        ---------------
        name - name of the place, must not be empty
        longitude - longitude of the place, must not be empty
        latitude - latitude of the place, must not be empty
        
        Returns
        ---------------
        a new Place instance that has been saved in the database.
        '''
        plc = cls(name=name,longitude=longitude,latitude=latitude)
        plc.save()
        return plc
    class Meta:
        unique_together = (("longitude", "latitude"),)
    def __unicode__(self):
        return name
    def __str__(self):
        return unicode(self).encode('utf-8')

    
   
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
    name            = models.CharField(max_length = 256, blank = False)
    organizations   = models.ManyToManyField(Organization)
    participants    = models.ManyToManyField(User, through = "Participation")
    place           = models.ManyToManyField(Place)
    desc            = models.TextField()
    keywords        = models.TextField()
    config          = models.CharField(max_length = 1024)
    cover           = models.ImageField(max_length = 1024)#change to ImageField after MEDIA_ROOT in settings.py is specified
    official_link   = models.CharField(max_length = 1024)
    create_time     = models.DateTimeField(auto_now_add = True)
    status          = models.CharField(max_length = 3, choices = STATUS_CHOICES)
    start_time      = models.DateTimeField(null = True)
    end_time        = models.DateTimeField(null = True)
    visits          = models.PositiveIntegerField(default = 0)
    
    @classmethod
    def create(cls,name,organizations):
        '''
        Create an activity.
        
        Parameters
        ---------------
        name - name of the activity, must not be empty
        orgranizations - organization queryset that raise the activity, must not be empty
        
        Returns
        ---------------
        a new Activity instance that has been saved to database
        '''
        act = cls(name=name)
        act.save()
        for org in organizations:
            act.organizations.add(org)
        act.save()
        return act
    def editInformation(self,field,val):
        '''
        Edit activity information.
        
        Parameters
        ---------------
        field - name of the field to edit, must not be empty
        val - new value
        
        Returns
        ---------------
        none
        '''
        if field == "name":
            self.name = val
        elif field == "place":
            self.place = val
        elif field == "desc":
            self.desc = val
        elif field == "official_link":
            self.official_link = val
        self.save()
    def addPlace(self,place):
        self.place.add(place)
        self.save()
    def removePlace(self,place):
        self.place.remove(place)
        self.save()
    def changeCover(self,cover):
        self.cover = cover
        self.save()
    def addPost(self,post):
        self.posts.add(post)
        self.save()
    def removePost(self,post):
        self.posts.remove(post)
        self.save()
    def publish(self):
        self.status = 'ONG'
        self.save()
    def cancel(self):
        self.status = 'ABD'
        self.save()
    def lock(self):
        self.status = 'FRZ'
        self.save()
    def finish(self):
        self.status = 'FIN'
        self.save()
    def getConfig(self):
        '''
        Get the values in config string.
        
        Parameters
        ---------------
        field - name of the field to edit, must not be empty
        
        Returns
        ---------------
        value of all the config
        '''
        pass
    def getConfig(self,name):
        '''
        Get the values in config string.
        
        Parameters
        ---------------
        field - name of the field to edit, must not be empty
        
        Returns
        ---------------
        value of the field
        '''
        pass
    def __unicode__(self):
        return name
    def __str__(self):
        return unicode(self).encode('utf-8')
    class Meta:
        pass
        #unique_together = (("name","organization"))
        ##The reason not to use unique_together here and in other models:https://code.djangoproject.com/ticket/702

class Post(models.Model):
    '''
    Forum posts.
    '''
    title           = models.CharField(max_length = 256, blank = False)
    content         = models.TextField(blank = False)
    organization    = models.ForeignKey(Organization)
    author          = models.ForeignKey(User)
    activity        = models.ForeignKey(Activity)
    create_time     = models.DateTimeField(auto_now_add = True)
    visits          = models.PositiveIntegerField(default = 0)
    @classmethod
    def create(cls,title,content,author,organization,activity):
        '''
        Create a post.
        
        Parameters
        ---------------
        title - title of the post
        content,author,organization,activity
        
        Returns
        ---------------
        a new Place instance that has been saved in the database.
        '''
        pst = cls(title=title,content=content,author=author,organization=organization,activity=activity)
        pst.save()
        return pst
    def __unicode__(self):
        return title
    def __str__(self):
        return unicode(self).encode('utf-8')
        
class Participation(models.Model):
    '''
    Participation describes the relationship between users and activities
    '''
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
    