from django.urls import path, re_path
from . import views
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    #path('api/user', views.UserList.as_view()),
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('logout/',views.logout_user, name='logout'),
    path('auth/', include('dj_rest_auth.urls')),
    path('makeprofile/', views.create_profile, name = 'createprofile'),
    re_path('profile/(?P<id>\d+)/',views.view_profile,name = 'myprofile'),
    #
]