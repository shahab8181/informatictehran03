from django.urls import path
from .views import EventsApiView


urlpatterns = [
    path('api/v1/events/', EventsApiView.as_view(), name='events-api')
]
