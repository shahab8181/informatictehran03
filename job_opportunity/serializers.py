from rest_framework import serializers
from .models import JobOpportunity


class JobOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpportunity
        exclude = [
            'is_active', 'created', 'updated_at'
        ]