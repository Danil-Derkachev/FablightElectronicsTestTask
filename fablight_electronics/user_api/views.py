from django.http import JsonResponse
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = UserSerializer(queryset, many=True).data
        return JsonResponse(data=data, safe=False)
