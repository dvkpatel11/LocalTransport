import re
from shutil import register_unpack_format
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # sourcery skip: assign-if-exp, reintroduce-else, swap-if-expression
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "user/user.html")

def login_view(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message" : "Invalid credentials"
            })

    # The line below calls login via the get request method
    return render(request, "user/login.html")

def logout_view(request):
    logout(request)
    return render(request, "user/login.html", {
        "message": "Logged out."
    })