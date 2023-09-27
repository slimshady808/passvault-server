from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
        
    ]
    return Response(routes)
