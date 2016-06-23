# coding=utf-8
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from .forms import LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.get_username()
        password = form.get_password()

        user = authenticate(username=username, password=password)
        if not user:
            context = {'error': u'Invalid user/password',
                       'form': self.get_form()}
            return self.render_to_response(context)

        login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('success')


class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'success.html'
