# README #


## Summary ##
A simple repo with a basic users django app

## Install ##

```
#!python

pip install -r requirements.txt
or just
pip install django

```

### Challenge tasks ###

* We want a substituted user model (I.e a custom user model) with an *email* field **see users.models**
* The user should be able to login with the email. *Requirement*: Implement a custom authentication backend and enable it. **see users.auth_backends.EmailAuthBackend**
* Migrations are not done. (Note: django 1.9)

### constraints ###
users.views.LoginView.form_valid is not allowed to have the execution flow changed. The authentication must go through the authbackends
The email field must be required on the new user model.

### Guidelines and how to test for success ###

* Login can be tested by default http://localhost:8000
* The success view is login protected and will present SUCCESS if login is successful otherwise a 404 is presented
* users can be created with python manage.py createsuperuser