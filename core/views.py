from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from . import models
from . import serializers
from rest_framework import status

class LoginView(ObtainAuthToken):
    pass 

class RegisterView(APIView):    
    def post(self, request):
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok',status=status.HTTP_201_CREATED)



