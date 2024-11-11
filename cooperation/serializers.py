from rest_framework import serializers
from .models import RequestingCooperation

class RequestingCooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestingCooperation
        exclude = [
            'created', 'updated_at'
        ]