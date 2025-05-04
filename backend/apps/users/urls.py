from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import (
    UserRetrieveUpdateDestroyView,
    CustomTokenObtainPairView,
    UserCreateView,
    ChangePasswordView,
    LogoutView,
    UserHintView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("user/", UserRetrieveUpdateDestroyView.as_view(), name="user"),
    path("user/change-password/", ChangePasswordView.as_view(), name="change_password"),
    path("hint/", UserHintView.as_view(), name="user_hint"),
]
