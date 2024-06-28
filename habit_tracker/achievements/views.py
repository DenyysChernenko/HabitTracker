from django.shortcuts import render
from .models import Achievement

# Create your views here.


def achievement_list(request):
    achievements = Achievement.objects.all()
    return render(request, 'achievements/achievement_list.html', {'achievements': achievements})
