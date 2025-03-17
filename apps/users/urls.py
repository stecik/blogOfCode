from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import (
    UserRetrieveUpdateDestroyView,
    CustomTokenObtainPairView,
    UserCreateView,
    ChangePasswordView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("user/", UserRetrieveUpdateDestroyView.as_view(), name="user"),
    path("user/change-password/", ChangePasswordView.as_view(), name="change_password"),
]
