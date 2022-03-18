from rest_framework import serializers
from .models import Vodka


class VodkaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "description", "created_at", "updated_at")
        model = Vodka
