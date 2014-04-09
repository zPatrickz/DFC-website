Volunteer2Here
===========

###Development Environment

`Apache` + `MySQL` + `Django (v1.5.1)` + `mod_wsgi (v3.4)` + `python (v2.7)`

Refer to `Setting.py` to checkout the settings used in project to access `MySQL`.

It is highly recommended to use **virtualenv**.

### Components

`xlutils` is an open python library for excel related operations. To install `xlutils`, please refer to http://pythonhosted.org/xlutils/installation.html, quick install:

	sudo pip install xlutils

`django-tagging` is an open django app for tagging. To install `django-tagging`, please refer to http://code.google.com/p/django-tagging/, quick install:

	sudo pip install django-tagging
	
`markdown` is an open django app for tagging. To install `makrdown`, please refer to http://pythonhosted.org//Markdown/index.html, quick install:

	sudo pip install markdown

### Configure

static files are collected in directory `ProjectRoot/static`, so add an alias in your VirtualHost:

	Alias /static/ /path/to/project/static/
	
Notice that for Django 1.7, please specify STATIC_ROOT, and specify it to a folder other than the 'static' folder



To use `ImageField`, please make sure you have installed Pillow. Use:
	
	sudo pip install Pillow
	
To put yourself away from case sensitive issues, please make sure your git is case sensitive, quick settings:
	
	git config --global core.ignorecase false
	
To quickly deploy the site, use:

	sudo python manage.py deploy --new


### Database

Development settings: 

	User: dfc 
	
	Password:123456
