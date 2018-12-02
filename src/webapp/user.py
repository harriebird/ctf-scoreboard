from hashlib import md5
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Flag, Capture, Team, TeamMember
from django.core.exceptions import ObjectDoesNotExist


def userLogin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
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
        if request.user.is_staff:
            return redirect('rank')
        else:
            return redirect('home')
    else:
        messages.error(request,'Please login to your account.')
        return redirect('login')


def userRegister(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    team = request.POST.get('team', '')

    if settings.TEAM_MODE:
        if not team:
            messages.error(request, 'Account registration failed. Please select a team.')
            return redirect('register')

        member_count = TeamMember.objects.filter(team_id=team).count()
        if member_count >= settings.TEAM_MEMBER_LIMIT:
            messages.error(request,
                           'Account registration failed. The team you selected has already {} members.'.format(
                               settings.TEAM_MEMBER_LIMIT))
            return redirect('register')
    match = User.objects.filter(username=username).count()
    if match == 0:
        user = User()
        user.username = username
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        team_member = TeamMember()
        team_member.user = user
        team_member.team = Team.objects.get(pk=team)
        team_member.save()
        messages.success(request, 'Account was successfully created. You can now log in.')
        return redirect('login')
    else:
        messages.error(request, 'Account registration failed. Please select another username.')
        return redirect('register')


def userCapture(request):
    code = request.POST.get('code', '')
    md5_code = md5(code.encode()).hexdigest()
    try:
        flag = Flag.objects.get(code=md5_code)
    except ObjectDoesNotExist:
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
    if settings.TEAM_MODE:
        cap_flags = []
        team = TeamMember.objects.filter(team=TeamMember.objects.get(user=request.user).team)
        for member in team:
            member_captures = Capture.objects.filter(user=member.user).order_by('-time')
            for capture in member_captures:
                cap_flags.append(capture)
    else:
        cap_flags = Capture.objects.filter(user=request.user).order_by('-time')
    return render(request, 'home.html', {'cap_flags': cap_flags, 'total_points': sumCapturePoints(cap_flags)})


def sumCapturePoints(captures):
    sum = 0
    for capture in captures:
        sum += capture.flag.points
    return sum
