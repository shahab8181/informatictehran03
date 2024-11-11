from rest_framework import serializers
from .models import Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        exclude = [
            'is_active', 'created', 'updated_at'
        ]