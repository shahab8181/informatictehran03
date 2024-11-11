from django.urls import path
from .views import ClassesApiView


urlpatterns = [
    path('api/v1/classes/', ClassesApiView.as_view(), name='classes-api')
]
