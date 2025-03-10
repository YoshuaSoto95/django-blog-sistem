from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def signin_page(request):
    return render(request, 'signin.html')
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
            username=username,
            password=password)
        if user is None:
            messages.error(request, "Username or Password is not valid, Try Again!")
            return redirect('accounts_security:signin_page')
        else:
            login(request, user)
            messages.success(request, "Login Successfully!!!")
            return redirect('dashboard:dashboard')
    else:
        messages.error(request, "Error, Your must login first")
        return redirect('accounts_security:signin_page')
    
def signout(request):
    logout(request)
    messages.success(request, "Logout Successfully!!!")
    return redirect('accounts_security:signin_page')
