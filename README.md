# README #


## Summary ##
Veridens challenge task.
The challenge is a common task when doing django projects. 
The pattern used fix the challenge is a standard pattern in django framework, it 
allows to plugin/customize behaviour in a non-intrusive way.

## Install ##

Use python 2.7
```
#!python

pip install -r requirements.txt
or just
pip install django

```

### Challenge tasks and requirements ###

**Highlevel description**
It's common to change the default login/authentication from a username to use email instead. 
The task is to customize and create model and the authentication mechanism for it.

* We want a substituted user model (I.e a custom user model) with an *email* field **see users.models**
* The user should be able to login with the email adress or username. *Requirement*: Implement a custom authentication backend and enable it. **see users.auth_backends.EmailAuthBackend**
* Create initial migrations. 

### Constraints ###
users.views.LoginView.form_valid is not allowed to have the execution flow changed. The authentication must go through the authbackends
The email field must be required on the new user model.

### Guidelines and how to test for success ###

* Login can be tested by default http://localhost:8000
* The success view is login protected and will present SUCCESS if login is successful otherwise a 404 is presented
* users can be created with python manage.py createsuperuser

### How to deliver result ###
Put project on github/bitbucket or zip source code into a single file (without .pyc files)
and email veridens.

