from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your views here.


def profile(request):
    return render(request, 'users/profile.html')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    authentication_form = CustomUserLoginForm
    success_url = reverse_lazy('profile')
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


