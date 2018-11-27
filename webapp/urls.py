from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('rank/', views.rank, name='rank'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
