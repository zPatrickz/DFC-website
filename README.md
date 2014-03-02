Volunteer2Here
===========

###Development Environment

`Apache` + `MySQL` + `Django (v1.5.1)` + `mod_wsgi (v3.4)` + `python (v2.7)`

Refer to `Setting.py` to checkout the settings used in project to access `MySQL`.

It is highly recommended to use **virtualenv**.

### Configure

static files are collected in directory `ProjectRoot/static`, so add an alias in your VirtualHost:

	Alias /static/ /path/to/project/static/


