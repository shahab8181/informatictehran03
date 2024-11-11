from django.urls import path
from .views import SupportMessageApiView

urlpatterns = [
    path('api/v1/contactus/', SupportMessageApiView.as_view(), name='contactus-api')
]
