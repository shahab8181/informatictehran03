from django.urls import path
from .views import RegisterApiView, LoginApiView, VerifyApiView

urlpatterns = [
    path('api/v1/register/', RegisterApiView.as_view(), name='register-api'),
    path('api/v1/login/', LoginApiView.as_view(), name='login-api'),
    path('api/v1/register/', VerifyApiView.as_view(), name='verify-api'),
]
