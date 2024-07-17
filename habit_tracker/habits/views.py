from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm
from django.utils.dateparse import parse_date
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class HabitDetail(DetailView):
    model = Habit
    context_object_name = 'habit'
    template_name = 'habits/habit_detail.html'


class HabitListView(ListView):
    model = Habit
    extra_context = {'title': 'Habit List'}
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        name = self.request.GET.get('name')
        start_date = self.request.GET.get('start_date')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if start_date:
            parsed_start_date = parse_date(start_date)
            if parsed_start_date:
                queryset = queryset.filter(start_date__gte=parsed_start_date)

        return queryset.select_related('user')


class CreateHabit(CreateView):
    form_class = HabitForm
    template_name = 'habits/add_habit.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateHabit(UpdateView):
    model = Habit
    fields = ['name', 'description', 'end_date', 'current_streak', 'is_completed']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('habit_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('habit_detail', kwargs={'pk': self.object.pk})


class DeleteHabit(DeleteView):
    model = Habit
    success_url = reverse_lazy("habit_list")
    template_name = "habits/delete_habit.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
