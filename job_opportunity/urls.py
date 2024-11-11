from django.urls import path
from .views import JobOpportunitiesApiView


urlpatterns = [
    path('api/v1/jobopportunities/', JobOpportunitiesApiView.as_view(), name='jobopportunities-api')
]
