from django.urls import path
from .views import profile, RegisterView, CustomLoginView


urlpatterns = [
    path('', profile, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
