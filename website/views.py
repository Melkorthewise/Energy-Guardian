from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
#from .models import Wattage, Login
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="toor",
    database="energy_guardian",
    port=3306,
)

mycursor = mydb.cursor()

@csrf_protect
def login(request):
    if request.method == "POST":
        #current_user_profile = request.user.profile
        email = request.POST.get("email")
        password = request.POST.get("password")
    
        mycursor.execute("SELECT * FROM login WHERE email_address = '{}'".format(email))
        myresult = mycursor.fetchall()

        for x in myresult:
            if x[1] == email and x[4] == password:
                request.session["user"] = x[0]
                response = redirect("main")
                return response

    return render(request, "login.html")


def main(request):
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

    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))

def home(request):
    return render(request, "index.html")

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
    del request.session["user"]
    
    return redirect("main")