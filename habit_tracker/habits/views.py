from django.shortcuts import render
from .models import Habit

# Create your views here.


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/habit_list.html', {'habits': habits})
