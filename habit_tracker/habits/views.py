from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm

# Create your views here.


def habit_detail(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    context = {
        'habit': habit
    }
    return render(request, 'habits/habit_detail.html', context)


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/habit_list.html', {'habits': habits})


def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES)
        if form.is_valid():
            habit = form.save()
            return redirect('habit_detail', habit_id=habit.pk)
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})
