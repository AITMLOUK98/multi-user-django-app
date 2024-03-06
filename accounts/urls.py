from django.urls import path
from . import views

urlpatterns = [
    # Token-based authentication
    path("token/", views.token_login, name="token_login"),

    # Username/password authentication
    path("login/", views.username_password_login, name="username_password_login"),

    # Logout
    path("logout/", views.logout_user, name="logout"),

    # User registration
    path("register/", views.user_register_view, name="register"),
]
