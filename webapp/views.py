from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Capture, Flag
from .user import userLogin, userLogout, userCheck, userRegister, userCapture, getUserCaptures
from django.db.models import Sum


# Create your views here.
# from django.shortcuts import get_object_or_404, render

def login(request):
    if request.method == 'POST':
        return userLogin(request)
    else:
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'user/login.html')

def logout(request):
    return userLogout(request)

def index(request):
    return userCheck(request)

def results(request):
    return render(request, 'home.html')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return getUserCaptures(request)
        elif request.method == 'POST':
            return userCapture(request)
    else:
        return userCheck(request)

def rank(request):
    ranking = User.objects.annotate(total_points=Sum('capture__flag__points')).exclude(is_staff=True).order_by('-total_points')
    return render(request, 'scoreboard.html', {'users': ranking})

def register(request):
    if request.method == 'POST':
        return userRegister(request)
    else:
        return render(request, 'user/register.html')
