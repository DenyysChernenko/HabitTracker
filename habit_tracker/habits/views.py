from django.shortcuts import render
from .models import Habit
from .forms import HabitForm

# Create your views here.


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/habit_list.html', {'habits': habits})


def add_habit(request):
    if request.method == 'POST':
        pass
    else:
        form = HabitForm()
        return render(request, 'habits/add_habit.html', {'form': form})
