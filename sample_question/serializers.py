from rest_framework import serializers
from .models import FieldOfStudy, Lesson



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = [
            'field_of_study', 'is_active', 
            'created', 'updated_at'
        ]

class FieldOfStudySerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(read_only=True, many=True)
    
    class Meta:
        model = FieldOfStudy
        exclude = [
            'is_active', 'created', 'updated_at'
        ]