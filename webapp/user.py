from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.core.exceptions import ObjectDoesNotExist

def userLogin(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password.')
        return render(request, 'user/login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def userCheck(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        messages.error(request,'Please login to your account.')
        return redirect('login')

def userRegister(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    first_name = request.POST.get('first_name','')
    last_name = request.POST.get('last_name','')
    match = User.objects.filter(username=username).count()
    if match == 0:
        user = User()
        user.username = username
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request,'Account was successfully created. You can now log in.')
        return redirect('login')
    else:
        messages.error(request,'Account registration failed. Please select another username.')
        return render(request, 'user/register.html')
