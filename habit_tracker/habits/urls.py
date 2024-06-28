from django.urls import path
from .views import habit_list
urlpatterns = [
    path('', habit_list, name='habit_list')
]
