from django.urls import path
from .views import UserList, CreateUser, UserDetail, profile


urlpatterns = [
    path('user-list/', UserList.as_view(), name='user_list'),
    path('add-user/', CreateUser.as_view(), name='add_user'),
    path('<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('', profile, name='profile'),

]
