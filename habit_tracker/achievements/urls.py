from django.urls import path
from .views import achievement_list

urlpatterns = [
    path('', achievement_list, name='achievement_list')
]
