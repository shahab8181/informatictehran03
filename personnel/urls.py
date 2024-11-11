from django.urls import path
from .views import TeachersApiView, StaffApiView


urlpatterns = [
   path('api/v1/teachers/', TeachersApiView.as_view(), name='teachers-api'), 
   path('api/v1/staff/', StaffApiView.as_view(), name='staff-api')
]
