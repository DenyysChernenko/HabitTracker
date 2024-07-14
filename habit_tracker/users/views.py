from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class UserList(ListView):
    model = User
    extra_context = {'title': 'User List'}

    def get_queryset(self):
        queryset = super().get_queryset()

        level = self.request.GET.get('level')
        experience = self.request.GET.get('experience')

        if level or experience:
            query = Q()

            if level:
                query &= Q(level__gte=level)
            if experience:
                query &= Q(experience__gte=experience)
            queryset = queryset.filter(query)

        return queryset


class UserDetail(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/user_detail.html'


class CreateUser(CreateView):
    form_class = UserForm
    template_name = 'users/add_user.html'


def profile(request):
    return render(request, 'users/profile.html')


class UpdateUser(UpdateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("user_list")

    def get_success_url(self):
        return reverse_lazy("user_detail", kwargs={"pk": self.object.pk})


class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')
    template_name = "users/delete_user.html"
