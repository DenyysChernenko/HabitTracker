from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create your views here.


def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user
    }
    return render(request, 'users/user_detail.html', context)


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', user_id=user.pk)
    else:
        form = UserForm()
    return render(request, 'users/add_user.html', {'form': form})
