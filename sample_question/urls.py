from django.urls import path
from .views import FieldsOfStudyApiView


urlpatterns = [
    path('api/v1/fieldsofstudy/', FieldsOfStudyApiView.as_view(), name='fields-of-study-api')
]
