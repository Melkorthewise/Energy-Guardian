from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('plotter', views.plotter, name='plotter'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
    path('register-device', views.register, name='register'),
]
