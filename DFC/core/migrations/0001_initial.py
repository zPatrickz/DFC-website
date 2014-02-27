# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=256),), ('email', models.EmailField(unique=True, max_length=254),), ('nickname', models.CharField(max_length=256),), ('password', models.CharField(max_length=256),), ('birthday', models.DateField(null=True),), ('gender', models.CharField(max_length=2, choices=(('MA', 'Male',), ('FM', 'Female',),)),), ('mobile', models.CharField(max_length=32),), ('qq', models.BigIntegerField(null=True),), ('avatar', models.CharField(max_length=1024),), ('desc', models.TextField(null=True),), ('create_time', models.DateTimeField(auto_now_add=True),), ('last_login', models.DateTimeField(),)],
            bases = (models.Model,),
            options = {},
            name = 'User',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Post',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Poster',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=256),), ('longitude', models.FloatField(),), ('latitude', models.FloatField(),)],
            bases = (models.Model,),
            options = {u'unique_together': set([('longitude', 'latitude',)])},
            name = 'Place',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(unique=True, max_length=256),), ('official_link', models.CharField(max_length=1024),), ('members', models.ManyToManyField(to='core.User'),)],
            bases = (models.Model,),
            options = {},
            name = 'Organization',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=256),), ('place', models.ForeignKey(to='core.Place', to_field=u'id'),), ('desc', models.TextField(),), ('keywords', models.TextField(),), ('config', models.CharField(max_length=1024),), ('cover', models.CharField(max_length=1024),), ('official_link', models.CharField(max_length=1024),), ('create_time', models.DateTimeField(auto_now_add=True),), ('status', models.CharField(max_length=3, choices=(('DFT', 'Draft',), ('ONG', 'Ongoing',), ('ABD', 'Abandoned',), ('FRZ', 'Frozen',), ('FIN', 'Finished',),)),), ('start_time', models.DateTimeField(null=True),), ('end_time', models.DateTimeField(null=True),), ('visits', models.PositiveIntegerField(default=0),), ('organization', models.ManyToManyField(to='core.Organization'),), ('participants', models.ManyToManyField(to='core.User'),), ('posts', models.ManyToManyField(to='core.Post'),), ('posters', models.ManyToManyField(to='core.Poster'),)],
            bases = (models.Model,),
            options = {},
            name = 'Activity',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('user', models.ForeignKey(to='core.User', to_field=u'id'),), ('organization', models.ForeignKey(to='core.Organization', to_field=u'id'),), ('role', models.CharField(max_length=3, choices=(('FND', 'Founder',), ('MGR', 'Manager',), ('MEM', 'Member',),)),), ('join_time', models.DateTimeField(auto_now_add=True),)],
            bases = (models.Model,),
            options = {u'unique_together': set([('user', 'organization',)])},
            name = 'Membership',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('user', models.ForeignKey(to='core.User', to_field=u'id'),), ('activity', models.ForeignKey(to='core.Activity', to_field=u'id'),), ('role', models.CharField(max_length=3, choices=(('ORG', 'Organizer',), ('MEM', 'Member',),)),), ('stage', models.CharField(max_length=3, choices=(('FLW', 'Follow',), ('APL', 'Apply',), ('ATD', 'Attended',),)),)],
            bases = (models.Model,),
            options = {u'unique_together': set([('user', 'activity',)])},
            name = 'Participation',
        ),
    ]
