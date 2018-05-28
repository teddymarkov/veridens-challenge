# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#substituting-a-custom-user-model

USERNAME_REGEX = '^[a-z+-]*$'


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username,
                          email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, is_admin, is_staff,
                         password=None):
        user = self.create_user(username, email, password)
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class User(AbstractBaseUser):

    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=300,
                              unique=True,
                              verbose_name='email address')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'is_admin', 'is_staff']

    def __str__(self):
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app {{}}?"""
        # Simplest possible answer: Yes, always
        return True
