from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from .forms import *
# Create your views here.
class MySignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth_forms/signup.html'

class MyLoginView(LoginView):
    form_class = MyLoginForm
    template_name = "auth_forms/login.html"

class MyPasswordResetView(PasswordResetView):
    form_class = MyPasswordResetForm
    html_email_template_name = "auth_forms/password_reset_email.html"
    template_name = "auth_forms/password_reset_form.html"
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MyPasswordResetConfirmForm
    template_name = "auth_forms/password_reset_confirm.html"