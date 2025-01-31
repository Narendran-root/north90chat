from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from chat import views

urlpatterns = [
    path("", views.chat_home, name="chat_home"),
    path("signup/", views.signup, name="signup"),
    path("login/", LoginView.as_view(template_name='chat/login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("chat/", views.chat_view, name="chat"),
]
