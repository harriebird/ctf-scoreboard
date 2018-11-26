from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.results, name='index'),
    path('home/', views.home, name='home'),
    path('rank/', views.rank, name='rank'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
]
