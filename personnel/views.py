from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from .models import Personnel
from .serializers import PersonnelSerializer

# Create your views here.

class TeachersApiView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = Personnel.objects.filter(personnel_type=Personnel.PersonnelTypeChoices.TEACHER, is_active=True)
    serializer_class = PersonnelSerializer


class StaffApiView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = Personnel.objects.filter(personnel_type=Personnel.PersonnelTypeChoices.STAFF, is_active=True)
    serializer_class = PersonnelSerializer