from django.shortcuts import render
from users.models import User
from django.views.generic import ListView
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserCreateForm
from django.urls import reverse_lazy

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LoginRequiredMixin,LogoutView):
    pass

class UserSignupView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/signup_user.html'
    success_url = reverse_lazy('users:login_user')