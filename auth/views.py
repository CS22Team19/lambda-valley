from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets, mixins
from rest_framework import permissions


from . import serializers


class UserCreateView(generics.CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    model = get_user_model()
    serializer_class = serializers.UserSerializer
