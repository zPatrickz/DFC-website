from django.db import models
from django.utils import timezone
from django.core import validators
from django.core.mail import send_mail
from django.contrib.auth import re
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext as _
from tagging.fields import *
from core.fields import *
from ckeditor.fields import RichTextField
from core.managers import EmailUserManager

# Core classes for DFC Project

# For general field usage, please refer to https://docs.djangoproject.com/en/1.6/ref/models/fields/
# For ManyToManyField usage, please refer to https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/
# and
# https://docs.djangoproject.com/en/1.6/topics/db/models/#intermediary-manytomany
# For model instance usage, please refer to https://docs.djangoproject.com/en/1.6/ref/models/instances/#model-instance-methods
# For tagging usage, please refer to https://github.com/brosner/django-tagging/blob/master/docs/overview.txt
# Use PhotoField instead of ImageField, and GalleryField for galleries

class BaseEmailUser(AbstractBaseUser, PermissionsMixin):
    """
    Abstract User Model: authenticated using email
    """
    
    email = models.EmailField(_('email address'), max_length=255, 
        unique=True, db_index=True)
    is_staff = models.BooleanField(_('staff status'), default=False, 
        help_text=_('Designates whether the user can log into the admin site'))
    is_active = models.BooleanField(_('active'), default=True, 
        help_text=_('Designates whether this user should be treated as active'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = EmailUserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the email
        """
        return self.email

    def get_short_name(self):
        """
        Returns the email
        """
        return self.email

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this user
        """
        send_mail(subject, message, from_email, [self.email])


class User(BaseEmailUser):
    """
    Concrete class of AbstractEmailUser
    This model is used as authentication model
    """
    
    first_name = models.CharField(_('first name'), max_length=30, 
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid first name.'), 'invalid')
        ])
    last_name = models.CharField(_('last name'), max_length=30, 
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid last name.'), 'invalid')
        ])
    birthday = models.DateTimeField(_('birthday'), blank=True, null=True, auto_now_add=False)
    qq = models.IntegerField(_('qq'), blank=True, null=True)
    telephone = models.CharField(_('telephone number'), max_length=20, blank=True)
    descriptions = models.CharField(_('descriptions'), max_length=512, blank=True)
    credit = models.IntegerField(_('credit value'), blank=True, default=0)
    
    def __unicode__(self):
        return self.email


class Organization(BaseEmailUser):
    """
    Another concrete class of AbstractEmailUser
    """
    
    username = models.CharField(_('orgnization name'), max_length=30, 
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid orgnization name'), 'invalid')
        ]) 
    organization_page = models.CharField(_('organization page link'), max_length=512, blank=True)
    pay_link = models.CharField(_('organization pay link'), max_length=512, blank=True)
    birthday = models.DateTimeField(_('birthday'), blank=True, null=True, auto_now_add=False)
    telephone = models.CharField(_('telephone number'), max_length=20, blank=True)
    descriptions = models.CharField(_('descriptions'), max_length=512, blank=True)
    credit = models.IntegerField(_('credit value'), blank=True, default=0)
    # members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, through='Membership')

    def __unicode__(self):
        return self.username


class Place(models.Model):
    name = models.CharField(max_length=256, blank=False)
    longitude = models.FloatField()
    latitude = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)
    @classmethod
    def create(cls, name, longitude, latitude):
        '''
        Create a place.
        # parameter name - name of the place, must not be empty
        # parameter longitude - longitude of the place, must not be empty
        # parameter latitude - latitude of the place, must not be empty
        # return a new Place instance that has been saved in the database.
        '''
        plc = cls(name=name,longitude=longitude,latitude=latitude)
        plc.save()
        return plc
    class Meta:
        unique_together = (("longitude", "latitude"),)
    def __unicode__(self):
        return '['+self.name+','+str(self.longitude)+','+str(self.latitude)+']'
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __eq__(self, other):
        return self.longitude == other.longitude and self.latitude == other.latitude
    

def get_photo_path( instance, filename ):
    return 'photo/'+str(instance.id)+'.jpg'

    
class Activity(models.Model):
    STATUS_CHOICES = (
        ('PRP','Proposal'),
        ('ONG','Ongoing'),
        ('ABD','Abandoned'),
        ('FRZ','Frozen'),
        ('FIN','Finished'),
    )
    CONTACT_METHOD_CHOICES = (
        ('USR','User'),
        ('MSG','MSG'),
        ('EML','EMail'),
        ('WCT','WeChat'),
    )
    
    DEFAULT_OVERFLOW_RATE = 133
    SHOW_ON_INDEXPAGE = 10
    
    name            = models.CharField(max_length = 256, blank = False)
    organizations   = models.ManyToManyField('Organization')
    participants    = models.ManyToManyField('User', through = "Participation",blank=True)
    places          = models.ManyToManyField('Place',blank=True)
    desc            = models.TextField(blank=True)
    content         = RichTextField(blank=True)
    content_file    = models.FileField(blank=True, null=True,upload_to='doc')
    is_private      = models.BooleanField(default=False)
    cover           = PhotoField(blank=True,null=True)# Always use PhotoField instead of ImageField
    
    required_participants   = models.PositiveIntegerField(null = True, blank = True)
    overflow_rate           = models.PositiveIntegerField(default = DEFAULT_OVERFLOW_RATE, blank = True)
    volunteer_requirements  = models.TextField(blank = True)
    volunteer_tasks         = models.TextField(blank = True)
    volunteer_obligation    = models.TextField(blank = True)
    volunteer_right         = models.TextField(blank = True)
    volunteer_hours         = models.PositiveIntegerField(null = True, blank = True)
    volunteer_auto_confirm  = models.BooleanField(default=True,blank=True)
    volunteer_auto_confirm_hour_ahead = models.PositiveIntegerField(default = 24,blank=True)
    notification_method     = models.CharField(max_length = 3,default = 'USR',choices = CONTACT_METHOD_CHOICES,blank=True)
    
    tags = TagField()# Use tagging here. Should be a single line text in a form. Make sure you have installed 'django-tagging'
    
    official_link   = models.URLField( blank=True)
    create_time     = models.DateTimeField(auto_now_add=True)
    update_time     = models.DateTimeField(auto_now=True)
    status          = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PRP',blank=True)
    start_time      = models.DateTimeField(null=True, blank=True)
    end_time        = models.DateTimeField(null=True, blank=True)
    visits          = models.PositiveIntegerField(default = 0)
    
    
    @classmethod
    def create(cls,name,organizations):
        '''
        Create an activity.
        # parameter name - name of the activity, must not be empty
        # parameter orgranizations - organization queryset that raise the activity, must not be empty
        # return a new Activity instance that has been saved to database
                    null if error occurs
        '''
        if not name:
            return None
        act = cls(name=name)
        act.save()
        if not organizations:
            return None
        for org in organizations:
            act.organizations.add(org)
        act.save()
        return act
    
    def update_name(self,val):
        if not val:
            return
        self.name = val
        self.save()
    def update_desc(self,val):
        if not val:
            return
        self.desc = val
        self.save()
    def update_official_link(self,val):
        if not val:
            return
        self.official_link = val
        self.save()
    def add_place(self,place):
        self.places.add(place)
        self.save()
    def remove_place(self,place):
        self.places.remove(place)
        self.save()
    '''def change_cover(self,cover):
        self.cover = cover
        self.save()'''
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
    def set_start_time(self,val):
        self.start_time = val
        self.save()
    def set_end_time(self,val):
        self.end_time = val
        self.save()
    def get_config(self):
        pass
    def get_config(self,name):
        pass
    '''def save(self, *args, **kwargs):
        if self.id is None:
            saved_cover = self.cover
            self.cover = None
            super(Activity, self).save(*args, **kwargs)
            self.cover = saved_cover
        super(Activity, self).save(*args, **kwargs)'''
    def __unicode__(self):
        return self.name
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __eq__(self, other):
        return self.name == other.name and self.organizations == other.organizations and self.place == other.place
    class Meta:
        pass
        #unique_together = (("name","organization"))
        ##The reason not to use unique_together here and in other models:https://code.djangoproject.com/ticket/702


class Album(models.Model):
    OWNER_TYPE_CHOICES = (
        ('ORG','Organization'),
        ('USR','User'),
        ('ACT','Activity'),
    )
    
    SHOW_ON_INDEXPAGE = 10
    
    title = models.CharField(max_length=256, blank=False)
    desc = models.TextField(blank=True)
    owner_type = models.TextField(max_length=3, choices=OWNER_TYPE_CHOICES, default = 'ACT')
    # owner_organization = models.ForeignKey(settings.AUTH_USER_MODEL,null=True)
    owner_user = models.ForeignKey('User',null=True)
    owner_activity = models.ForeignKey('Activity',null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return unicode(self).encode('utf-8')
        
class Photo(models.Model):
    photo = models.ImageField(max_length = 1024, upload_to=get_photo_path)
    desc = models.TextField(blank=True)
    album = models.ForeignKey('Album')
    create_time = models.DateTimeField(auto_now_add=True)
    visits = models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
        if self.id is None:
            saved_photo = self.photo
            self.photo = None
            super(Photo, self).save(*args, **kwargs)
            self.photo = saved_photo
        super(Photo, self).save(*args, **kwargs)
    def __unicode__(self):
        return 'Photo'+str(self.id)
    def __str__(self):
        return unicode(self).encode('utf-8')

        
class Post(models.Model):
    '''
    Forum posts.
    '''
    title = models.CharField(max_length=256, blank=False)
    content = models.TextField(blank=False)
    # organization = models.ForeignKey(settings.AUTH_USER_MODEL)
    author = models.ForeignKey('User')
    activity = models.ForeignKey('Activity')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    visits = models.PositiveIntegerField(default=0)
    @classmethod
    def create(cls,title,content,author,organization,activity):
        '''
        Create a post.
        # parameter title - title of the post
        # parameter content,author,organization,activity
        # return a new Place instance that has been saved in the database.
        '''
        pst = cls(title=title,content=content,organization=organization,activity=activity)
        pst.save()
        pst.authors.add(author)
        return pst
    def update_title(self,val):
        '''
        Edit the content of the post.
        # parameter val - new value
        # return none
        
        Todos
        ---------------
        check if user is authorized
        '''
        self.title = val
        self.save()
    def update_content(self,val):
        '''
        Edit the content of the post.
        # parameter val - new value
        # return none
        
        Todos
        ---------------
        check if user is authorized
        '''
        self.content = val
        self.save()
    def __unicode__(self):
        return self.title
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __eq__(self, other):
        return self.organization == other.organization and self.activity == other.activity and self.title == other.title
        

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
    user = models.ForeignKey('User')
    activity = models.ForeignKey('Activity')
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    stage = models.CharField(max_length=3, choices=STAGE_CHOICES)
    class Meta:
        unique_together=(("user","activity"))
        

class Membership(models.Model):
    '''
    Membership describes the relationship between users and organizations
    '''
    
    user = models.ForeignKey('User')
    organization = models.ForeignKey('Organization')
    join_time = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = (("user","organization"))
    