from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name="main"),
    path('home', views.home, name="home"),
]
