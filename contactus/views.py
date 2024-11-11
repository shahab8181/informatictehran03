from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from .models import SupportMessage
from .serializers import SupportMessageSerializer

# Create your views here.

class SupportMessageApiView(CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = SupportMessage.objects.all()
    serializer_class = SupportMessageSerializer
    