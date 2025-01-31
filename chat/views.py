# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

# Homepage view
def chat_home(request):
    if request.user.is_authenticated:
        return redirect("chat")  # Redirect to chat if the user is logged in
    return render(request, "chat/login.html")  # Homepage if not logged in

# Signup view
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("chat")  # Redirect to chat after signup
    else:
        form = UserCreationForm()
    return render(request, "chat/signup.html", {"form": form})

# Chat view (only for logged-in users)
@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude current user from list
    return render(request, "chat/chat.html", {"users": users})
