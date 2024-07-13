from django.urls import path
from .views import user_list, add_user, user_detail


urlpatterns = [
    path('', user_list, name='user_list'),
    path('add-user/', add_user, name='add_user'),
    path('<int:user_id>/', user_detail, name='user_detail')
]
