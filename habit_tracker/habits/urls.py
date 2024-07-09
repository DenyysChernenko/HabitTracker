from django.urls import path
from .views import habit_list, add_habit
urlpatterns = [
    path('', habit_list, name='habit_list'),
    path('habits/add-habit', add_habit, name='add_habit'),

]
