from django.urls import path
from .views import xp_log_list

urlpatterns = [
    path('', xp_log_list, name='xp_log_list')
]
