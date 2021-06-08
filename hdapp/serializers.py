#from rest_framework import serializers
from hdapp.models import Neighbourhood, User
from django.urls import path, include
from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets


#class UserSerializer(serializers.ModelSerializer):
  #class Meta:
      #model = User
      #fields = "__all__"

#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer

    #router = routers.DefaultRouter()
    #router.register(r'users', UserViewSet)

#class HoodSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Neighbourhood
        #fields = "__all__"