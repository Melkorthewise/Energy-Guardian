from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
#from .models import Wattage, Login
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from .connect import *


@csrf_protect
def login(request):
    if request.method == 'POST':
        database = connecter()
        username = request.POST.get("username")
        password = request.POST.get("password")

        if database.login(username, password):
            return redirect('main')
        
        elif  username == "" or password == "":
            return render(request, 'login.html')
            
        else:
            return render(request, 'login.html', context={"error_message":"Wrong e-mail address / password"})
    
    return render(request, 'login.html')

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def home(request):
    return render(request, "index.html")

def signUp(request):
    if request.method == 'POST':
        database = connecter()
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("secondName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        database.signUp(email, firstName, lastName, password)
        
    
    return render(request, 'signUp.html')