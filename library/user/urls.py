from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import UserCreateView,UserLoginView,UserLogoutView,UserChangePasswordView,UserForgotPasswordView
urlpatterns = [
    path("create", UserCreateView.as_view()),
    path('login', UserLoginView.as_view()),
    path('logout', UserLogoutView.as_view()),
    path('changepassword',UserChangePasswordView.as_view()),
    path('forgotpassword',UserForgotPasswordView.as_view()),
    # path('profile',UserProfileView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
   

    
]

