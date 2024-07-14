from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class UserList(ListView):
    model = User
    extra_context = {'title': 'User List'}


class UserDetail(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'


class CreateUser(CreateView):
    form_class = UserForm
    template_name = 'users/add_user.html'


def profile(request):
    return render(request, 'users/profile.html')
