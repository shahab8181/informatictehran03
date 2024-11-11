from django.urls import path
from .views import GalleyApiView


urlpatterns = [
    path('api/v1/gallery/', GalleyApiView.as_view(), name='gallery-api')
]
