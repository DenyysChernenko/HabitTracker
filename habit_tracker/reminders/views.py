from django.shortcuts import render
from .models import Reminder

# Create your views here.


def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})
