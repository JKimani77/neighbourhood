from django.shortcuts import render
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from .models import *
#from rest_framework.permissions import IsAuthenticated
from django.http import Http404

def index(request):
    neighbourhoods = Neighbourhood.objects.all()
    posts = Post.objects.all()
    departments = Department.objects.all()

    return render(request, 'index.html', {'neighbourhoods':neighbourhoods, 'posts':posts, 'departments':departments} )

