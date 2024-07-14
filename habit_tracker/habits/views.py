from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm
from django.views.generic import ListView, DetailView, CreateView

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
