Volunteer2Here
===========

###Development Environment

`Apache` + `MySQL` + `Django (v1.5.1)` + `mod_wsgi (v3.4)` + `python (v2.7)`

Refer to `Setting.py` to checkout the settings used in project to access `MySQL`.

It is highly recommended to use **virtualenv**.

### Components

`openpyxl` is an open python library for excel related operations
To install openpyxl, please refer to http://openpyxl.readthedocs.org/en/latest/#getting-the-source, quick install:

	`pip install openpyxl`
	

### Configure

static files are collected in directory `ProjectRoot/static`, so add an alias in your VirtualHost:

	Alias /static/ /path/to/project/static/
	
Notice that for Django 1.7, please specify STATIC_ROOT, and specify it to a folder other than the 'static' folder



To use `ImageField` and `openpyxl`, please make sure you have installed Pillow. Use:
	`sudo pip install Pillow`


### Database

Development settings: 
	User: dfc 
	Password:123456
