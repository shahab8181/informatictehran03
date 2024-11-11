from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .models import RequestingCooperation
from .serializers import RequestingCooperationSerializer

# Create your views here.

class RequestingCooperationApiView(CreateAPIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    queryset = RequestingCooperation.objects.all()
    serializer_class = RequestingCooperationSerializer