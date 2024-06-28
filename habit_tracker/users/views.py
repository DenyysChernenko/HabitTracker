from django.shortcuts import render
from .models import User

# Create your views here.


def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {'users': users})
