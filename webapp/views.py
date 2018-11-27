from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Capture, Flag
from .user import userLogin, userLogout, userCheck, userRegister
from django.db.models import Sum


# Create your views here.
# from django.shortcuts import get_object_or_404, render

def login(request):
    if request.method == 'POST':
        return userLogin(request)
    else:
        return render(request, 'user/login.html')

def logout(request):
    return userLogout(request)

def index(request):
    return userCheck(request)

def results(request):
    return render(request, 'home.html')

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        code = request.POST.get('code','')
        flag = Flag.objects.get(code=code)
        user_flag = Capture.objects.filter(user=request.user, flag=flag).count()
        if user_flag == 0:
            Capture.objects.create(user=request.user, flag=flag)
        return render(request, 'home.html')

def rank(request):
    ranking = User.objects.annotate(total_points=Sum('capture__flag__points')).exclude(is_staff=True).order_by('-total_points')
    for user in ranking:
        print('{} {}'.format(user, user.total_points))
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        return userRegister(request)
    else:
        return render(request, 'user/register.html')
