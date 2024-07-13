from django.urls import path

from .views import UserList, UserRetrieveUpdateDestroy, UserByToken

urlpatterns = [
    path('user/by/token/', UserByToken.as_view(), name='user_by_token'),
    path('users', UserList.as_view(), name='users_list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroy.as_view(), name='user_retrieve_update_destroy'),
]
