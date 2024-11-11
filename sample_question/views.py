from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from .models import FieldOfStudy
from .serializers import FieldOfStudySerializer

# Create your views here.

class FieldsOfStudyApiView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = FieldOfStudy.objects.filter(is_active=True)
    serializer_class = FieldOfStudySerializer