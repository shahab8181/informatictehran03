from rest_framework import serializers
from .models import SupportMessage

class SupportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportMessage
        exclude = [
            'is_read_by_admin', 'created', 'updated_at'
        ]