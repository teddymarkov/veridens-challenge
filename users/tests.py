# coding=utf-8
from django.contrib.auth import authenticate
from django.test import TestCase

from users import models


class TestUser(TestCase):
    def test_login_email(self):
        User = models.User
        user = User.objects.create(
            username='testtest1',
            email='test1@test.com'
        )
        user.set_password('test')
        user.is_active = True
        user.save()
        result = authenticate(username='test1@test.com', password='test')
        self.assertEqual(result, user)

    def test_login_username(self):
        User = models.User
        user = User.objects.create(
            username='testtest2',
            email='test2@test.com'
        )
        user.set_password('test')
        user.is_active = True
        user.save()
        result = authenticate(username='test2@test.com', password='test')
        self.assertEqual(result, user)
