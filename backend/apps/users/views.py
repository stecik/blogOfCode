from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.utils.timezone import now

CustomUser = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        password = request.data.get("password")
        if not password:
            return Response({"error": "Password is required."}, status=400)
        if not user.check_password(password):
            return Response({"error": "Incorrect password."}, status=400)
        user.delete()
        return Response({"detail": "User deleted successfully"}, status=204)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        user = self.get_object()
        password = request.data.get("old_password")
        if not password:
            return Response({"error": "Old password is required."}, status=400)
        if not user.check_password(password):
            return Response({"error": "Incorrect old password."}, status=400)
        if serializer.is_valid():
            serializer.update(self.get_object(), serializer.validated_data)
            return Response({"detail": "Password changed successfully"}, status=200)
        return Response(serializer.errors, status=400)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        username = request.data.get("username")
        if username:
            user = CustomUser.objects.get(username=username)
            user.is_online = True
            user.last_login = now()
            user.save()
            return response
        return response


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            user.is_online = False
            user.save()
            return Response({"detail": "User logged out successfully"}, status=200)
        except Exception:
            return Response({"error": "An error occurred during logout"}, status=400)
