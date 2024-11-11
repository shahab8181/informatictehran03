from django.urls import path
from .views import ArticlesApiView

urlpatterns = [
    path('api/v1/articles/', ArticlesApiView.as_view(), name='articles-api')
]
