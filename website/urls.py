from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
    path('register-device', views.register, name='register'),
    path('accountDeleted', views.delete, name='accountDeleted'),
    path('update', views.update, name='update'),
]
