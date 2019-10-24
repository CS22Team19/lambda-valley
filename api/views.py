from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets, mixins

from . import models
from . import serializers


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
