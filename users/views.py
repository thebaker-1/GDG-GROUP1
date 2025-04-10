from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your views here.
from .models import User
from .serializers import UserUpdateSerializer,RegisterSerializer, UserProfileSerializer
from rest_framework import status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# for login 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if not user.is_active:
            raise serializers.ValidationError(_("User account is inactive."))
        token = super().get_token(user)

        # Add custom claims if needed
        token['username'] = user.username
        return token

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
# for register
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for logout
class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token or token already blacklisted."}, status=status.HTTP_400_BAD_REQUEST)

# for user id

class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        try:
            user = self.queryset.get(id=user_id)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# for user update

class UserUpdateView(APIView):
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)