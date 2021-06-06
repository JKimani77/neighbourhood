from django.urls import path, re_path
from . import views


urlpatterns = [
    #path('api/user', views.UserList.as_view()),
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('logout/',views.logout_user, name='logout'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/v1/create_hood',views.HoodList.as_view()),
    #path('api/v1/hoods', views.AllHoodsList.as_view()),
    #path('api/v1/view_hood/<int:pk>', views.SingleHoodList.as_view()),
    #path('api/v1/post', views.CreatePostView.as_view()),
    #path('api/v1/create_business/<int:pk>', views.CreateBusinessView.as_view()),
    #path('api/v1/create_dept/<int:pk>', views.CreateDepartmentView.as_view()),
    #path('api/v1/profile/<int:pk>/<int:id>', views.EditProfileView.as_view())

]