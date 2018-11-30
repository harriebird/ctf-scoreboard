from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Flag, Capture
from django.core.exceptions import ObjectDoesNotExist
from hashlib import md5

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

def userCapture(request):
    code = request.POST.get('code','')
    md5_code = md5(code.encode()).hexdigest()
    try:
        flag = Flag.objects.get(code=md5_code)
    except:
        messages.error(request, 'Flag does not exist. Better try again!')
        return getUserCaptures(request)
    user_flag = Capture.objects.filter(user=request.user, flag=flag).count()
    if user_flag == 0:
        Capture.objects.create(user=request.user, flag=flag)
        messages.success(request, 'Flag was successfully captured.')
    else:
        messages.error(request, 'Flag already captured. Better find another flag..')
    return getUserCaptures(request)

def getUserCaptures(request):
    cap_flags = Capture.objects.filter(user=request.user).order_by('-time')
    return render(request, 'home.html', {'cap_flags':cap_flags, 'total_points':sumCapturePoints(cap_flags)})

def sumCapturePoints(captures):
    sum = 0
    for capture in captures:
        sum += capture.flag.points
    return sum
