from rest_framework import serializers

from . import models


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = []
        model = models.Player
