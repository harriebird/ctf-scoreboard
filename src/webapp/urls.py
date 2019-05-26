from django.urls import path, re_path
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('rank/', views.rank, name='rank'),
    path('register/', views.register, name='register'),
    path('history/', views.history, name='history'),
    re_path(r'^static/(?P<path>.*)$', views.showfile),
]

if settings.TEAM_MODE:
    urlpatterns += [
        path('teams/', views.teams, name='teams'),
    ]
