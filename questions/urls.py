from django.urls import path
from .views import QuestionAnswersApiView

urlpatterns = [
    path('api/v1/question-answers/', QuestionAnswersApiView.as_view(), name='question-answers-api')
]
