import re
from django.shortcuts import render, redirect
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login, logout
#rest framework not reading from installed apps 
#from rest_framework.permissions import IsAuthenticated
from django.http import Http404

def index(request):
    neighbourhoods = Neighbourhood.objects.all()
    posts = Post.objects.all()
    departments = Department.objects.all()
    businesses = Business.objects.all()
    return render(request, 'index.html', {'neighbourhoods':neighbourhoods, 'posts':posts, 'departments':departments, "businesses":businesses} )





def login(request):
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            

            user = authenticate(request, username=username,password=password, )
            
            if user.is_active:
                login(request,user)
                return redirect(index)
            else:
                return "Your account is inactive"
    else:
        form = LoginForm()
    return render(request, 'auth/login.html',{"form":form})

def logout_user(request):
    logout(request)
    return redirect(index)

def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(index)
    else:
        form = ProfileForm()
    return render(request, 'makeprofile.html',{"form":form})




def view_profile(request, id):
    
    current_user = request.user
    profile = Profile.objects.filter(id = id).all()
    return render(request, 'myprofile.html',{"profile":profile}) #{"projects":projects})

def view_hood_details(request,id):
    hood = Neighbourhood.objects.filter(id = id).all()
    return render(request,'details.html', {"hood":hood} )
















































































































    #def register(request):
    #if request.method == 'POST':
        #form = CustomUserCreationForm(data=request.POST)
        #if form.is_valid():
        
            #user = authenticate(request)
            #if user.is_authenticated:
                #return redirect(login)
            #else:
                #return "Unable to register"

   # else:
        #form = CustomUserCreationForm()
    #return render(request, 'django-registration/registration_form.html',{"form":form})