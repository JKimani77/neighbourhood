from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Neighbourhood,Profile,Department, Business, Post
from .serializers import UserSerializer, HoodSerializer, PostSerializer, ProfileSerializer,BusinessSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404