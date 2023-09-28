from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
        
    ]
    return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)

        token['username']=user.username
        token['email'] = user.email

        return token

class MytokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        # Create a serializer instance with the request data
        serializer = UserProfileSerializer(data=request.data)

        # Validate the serializer data
        if serializer.is_valid():
            # Hash the password before saving it to the database
            password = make_password(request.data['password'])
            serializer.validated_data['password'] = password

            # Save the user to the database
            serializer.save()
            

            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # If validation fails, return the validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
