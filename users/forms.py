# coding=utf-8
from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(label='Username/Email')
    password = forms.CharField(widget=PasswordInput, label='Password')

    def get_username(self):
        return self.cleaned_data['username']

    def get_password(self):
        return self.cleaned_data['password']
