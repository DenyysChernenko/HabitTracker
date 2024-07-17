from django.urls import path
from .views import profile, RegisterView, CustomLoginView, home
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
