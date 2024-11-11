from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from .models import User, Otp
from .serializers import RegisterSerializer, LoginSerializer, VerifySerializer

# Create your views here.

class RegisterApiView(CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    serializer_class = RegisterSerializer
    
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': '.کد برای شماره موبایل شما ارسال شد'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': '!خطای سیستمی'}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginApiView(CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    serializer_class = LoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            try:
                user = User.objects.get(phone_number__iexact=serializer.validated_data('phone_number'))
                if not user.check_password(user.password):
                    raise User.DoesNotExist
                else:
                    TOKEN = Token.objects.get(user=user)
            except User.DoesNotExist:
                return Response({'status': '!شماره موبایل یا کلمه عبور نامعتبر میباشد'}, status=status.HTTP_404_NOT_FOUND)
            except Token.DoesNotExist:
                return Response({'status': '!خطای سیستمی'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'token': TOKEN.key}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'status': '!خطای سیستمی'}, status=status.HTTP_400_BAD_REQUEST)
            
            
            
class VerifyApiView(CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    serializer_class = VerifySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            try:
                otp_code = Otp.objects.get(phone_numner=serializer.validated_data('phone_number'), code=serializer.validated_data('code'))
            except Otp.DoesNotExist:
                return Response({'status': '!کد نامعتبر میباشد'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'token': otp_code.user.auth_token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': '!خطای سیستمی'}, status=status.HTTP_400_BAD_REQUEST)
    
    
           
            
            
