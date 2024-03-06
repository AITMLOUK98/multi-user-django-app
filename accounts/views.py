from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegisterSerializer

@api_view(["POST"])
def token_login(request):
    token = request.data.get("token")
    if token:
        try:
            user = Token.objects.get(key=token).user
            if user.is_authenticated:
                return Response({"message": "Login successful", "username": user.username}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def username_password_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username and password:
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful", "token": user.auth_token.key}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    return Response({"message": "User is not authenticated"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            return Response({"message": "Account has been created", "username": account.username, "email": account.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
