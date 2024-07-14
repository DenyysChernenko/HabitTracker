from django.urls import path
from .views import HabitListView, CreateHabit, HabitDetail, UpdateHabit, DeleteHabit
urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('habits/add-habit', CreateHabit.as_view(), name='add_habit'),
    path('<int:pk>/', HabitDetail.as_view(), name='habit_detail'),
    path('<int:pk>/edit/', UpdateHabit.as_view(), name='habit_update'),
    path('<int:pk>/delete/', DeleteHabit.as_view(), name='habit_delete')
]
