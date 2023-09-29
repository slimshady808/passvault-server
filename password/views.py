from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from .serializers import PasswordSerializer
from .models import Password
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
        
    ]
    return Response(routes)

class PasswordCreateListView(CreateAPIView):
    queryset=Password.objects.all()
    serializer_class = PasswordSerializer

class PasswordListByUserIDView(ListAPIView):
    serializer_class = PasswordSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Assuming 'user_id' is the URL parameter name
        queryset = Password.objects.filter(user=user_id)  # Adjust the field name as per your model
        return queryset
    
@api_view(['DELETE'])
def delete_password(request, id):
    try:
        password=Password.objects.get(id=id)
    except Password.DoesNotExist:
        return Response({'message': 'password not found'}, status=status.HTTP_404_NOT_FOUND)

    password.delete()
    return Response({'message': 'password deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
