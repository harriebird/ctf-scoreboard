from django.shortcuts import render, redirect
from django.conf import settings
from django.views.static import serve
from .models import User, Team, TeamMember, Capture
from .user import userLogin, userLogout, userCheck, userRegister, userCapture, getUserCaptures
from django.db.models import Sum


# Create your views here.
# from django.shortcuts import get_object_or_404, render

def login(request):
    if request.method == 'POST':
        return userLogin(request)
    else:
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('rank')
            else:
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
        if request.user.is_staff:
            return redirect('rank')
        if request.method == 'GET':
            return getUserCaptures(request)
        elif request.method == 'POST':
            return userCapture(request)
    else:
        return userCheck(request)


def rank(request):
    ranking = []
    if settings.TEAM_MODE:
        ranking = Team.objects.annotate(
            total_points=Sum('teammember__user__capture__flag__points')).order_by('-total_points')
    else:
        ranking = User.objects.annotate(
            total_points=Sum('capture__flag__points')).exclude(is_staff=True).order_by('-total_points')
    return render(request, 'scoreboard.html', {'data': {'ranking': ranking, 'team_mode': settings.TEAM_MODE}})


def register(request):
    if request.method == 'POST':
        return userRegister(request)
    else:
        teams = Team.objects.all()
        return render(request, 'user/register.html', {'data': {'teams': teams, 'team_mode': settings.TEAM_MODE}})


def teams(request):
    team_members = []
    team_list = Team.objects.all()
    for team in team_list:
        members = TeamMember.objects.filter(team=team)
        team_members.append({'name': team.name, 'members': members})
    return render(request, 'teams.html', {'data': {'teams': team_members}})


def showfile(request, path):
    return serve(request, path, settings.STATIC_ROOT)


def history(request):
    logs = Capture.objects.all().order_by('-time')
    return render(request, 'history.html', {'data': {'history': logs, 'team_mode': settings.TEAM_MODE}})
