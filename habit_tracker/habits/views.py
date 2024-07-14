from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm
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


class CreateHabit(CreateView):
    form_class = HabitForm
    template_name = 'habits/add_habit.html'


class UpdateHabit(UpdateView):
    model = Habit
    fields = ['name', 'description', 'end_date', 'current_streak', 'is_completed']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('habit_list')

    def get_success_url(self):
        return reverse_lazy('habit_detail', kwargs={'pk': self.object.pk})


class DeleteHabit(DeleteView):
    model = Habit
    success_url = reverse_lazy("habit_list")
    template_name = "habits/delete_habit.html"
