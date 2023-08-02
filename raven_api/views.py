from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Project,User
from .serializers import ProjectSerializer,RegisterSerializer
from rest_framework.decorators import  permission_classes,authentication_classes
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

def index(request):
    return HttpResponse(" Demo Project")

@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
class Projectser(ListCreateAPIView) :
    queryset = Project.objects.all()
    serializer_class  = ProjectSerializer


@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
class Project_ser(RetrieveUpdateDestroyAPIView):
    queryset  = Project.objects.all()
    serializer_class  = ProjectSerializer

@permission_classes((AllowAny,))
class register_user(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    
    