from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
#from .models import Wattage, Login
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
import mysql.connector
from .connect import *

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="toor",
    database="energy_guardian",
    port=3306,
)

mycursor = mydb.cursor()

def home(request):
    return render(request, "index.html")

@csrf_protect
def login(request):
    try:
        user = request.session["user"]
        return redirect('main')
    except KeyError:
        pass

    if request.method == "POST":
        #current_user_profile = request.user.profile
        # Ophalen email en wachtwoord van ingevulde formulier
        email = request.POST.get("email")
        password = request.POST.get("password")
    
        # Het uitvoeren van de query met de opgehaalde gegevens
        mycursor.execute("SELECT * FROM login WHERE email_address = '{}' and password = '{}'".format(email, password))
        myresult = mycursor.fetchall()

        for x in myresult:
            # Checken of het de juiste gegevens zijn
            if x[1] == email and x[4] == password:
                request.session["user"] = x[0]
                response = redirect("main")
                return response

    return render(request, "login.html")


def main(request):
    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')
    
    mycursor.execute("SELECT FirstName FROM login where UserID = '{}'".format(user))
    myresult = mycursor.fetchall()

    for x in myresult:
        context = {
            'user': x,
        }

    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))

def plotter(request):
    user = request.session["user"]

    # user = request.COOKIES.get('user')
    if user is None:
        response = redirect("login")
        return response
    
    mycursor.execute("SELECT FirstName FROM login where UserID = '{}'".format(user))
    myresult = mycursor.fetchall()

    for x in myresult:
        context = {
            'user': x,
        }

    template = loader.get_template("plotter.html")
    return HttpResponse(template.render(context, request))

def logout(request):
    try:
        del request.session["user"]
        return redirect('login')
    except KeyError:
        pass
    
    return redirect("main")

def signup(request):
    try:
        user = request.session["user"]
        return redirect('main')
    except KeyError:
        pass

    if request.method == 'POST':
        database = connecter()
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("secondName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        database.signUp(email, firstName, lastName, password)

        return redirect('login')
        
    
    return render(request, 'signUp.html')