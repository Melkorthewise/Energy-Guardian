from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
#from .models import Wattage, Login
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
import mysql.connector
from .connect import *


# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="energy_guardian",
    port=3306,
)

mycursor = mydb.cursor()


#Home pagina
def home(request):
    return render(request, "index.html")


# Login pagina
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
        mycursor.execute("SELECT * FROM users WHERE Email_Address = '{}' and Password = '{}'".format(email, password))
        myresult = mycursor.fetchall()

        print(email, password, myresult)

        for x in myresult:
            # Checken of het de juiste gegevens zijn
            if x[1] == email and x[4] == password:
                request.session["user"] = x[0]
                response = redirect("main")
                return response

    return render(request, "login.html")


# Main page with dashboard
def main(request):
    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')
    
    # Sorteren op datum waar die kijkt naar bijvoorbeeld de afgelopen 24 uur
    mycursor.execute("SELECT DeviceID, Volt, Ampere, latestpulltime FROM wattage where DeviceID in (SELECT DeviceID FROM Device WHERE UserID = '{}')".format(user))
    #voltage = [row[1] for row in mycursor.fetchall()]
    #amperage = [row[2] for row in mycursor.fetchall()]
    data = [row[1] for row in mycursor.fetchall()]
    time = [row[3] for row in mycursor.fetchall()]

    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    username = user_tuple[0] if user_tuple else None

    mycursor.execute("SELECT Name_Device FROM Device WHERE UserID = '{}'".format(user))
    device = mycursor.fetchone()    

    print(user, device)
    
    context = {
        'user': username,
        'voltage': data,
        'device': device,
    }
            
    # print(type(context), context)

    print("Test:", context)

    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))


# Plotter pagina
def plotter(request):
    user = request.session["user"]

    # user = request.COOKIES.get('user')
    if user is None:
        response = redirect("login")
        return response
    
    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    myresult = mycursor.fetchall()

    for x in myresult:
        context = {
            'user': x,
        }

    template = loader.get_template("plotter.html")
    return HttpResponse(template.render(context, request))


# Logout function
def logout(request):
    try:
        del request.session["user"]
        return redirect('login')
    except KeyError:
        pass
    
    return redirect("main")


# Signup pagina maken
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