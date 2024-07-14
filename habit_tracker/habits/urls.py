from django.urls import path
from .views import HabitListView, CreateHabit, HabitDetail
urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('habits/add-habit', CreateHabit.as_view(), name='add_habit'),
    path('<int:pk>/', HabitDetail.as_view(), name='habit_detail'),

]
