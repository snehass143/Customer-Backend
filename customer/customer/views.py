from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .searilizers import  customerSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def sample(request):
        data = {'message': 'Hello, this is a sample API!'}
        return Response(data, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    password1 = request.data.get('password1')

    if password != password1:
        return Response({'error': 'Confirmation Password is Wrong'}, status=HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username= username, email=email, password=password)
    user.save() 

    return Response({'Success': 'User Creation Successfully'}, status=HTTP_201_CREATED)




@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
   
    user = authenticate (username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key},status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((AllowAny,))

def allusers(request):
    users = User.objects.all()
    serializer = customerSerializer(users, many=True) 
    return Response(serializer.data)