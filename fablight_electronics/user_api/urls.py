from django.urls import path

from .views import UserList, UserRetrieveUpdateDestroy

urlpatterns = [
    path('users', UserList.as_view(), name='users_list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroy.as_view(), name='user_retrieve_update_destroy'),
]
