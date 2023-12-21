from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.core.serializers.json import DjangoJSONEncoder

# Import non-Django libraries
import mysql.connector
import json
from datetime import datetime, timedelta

# Import other files
from .connect import *
from .math import *

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

    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    username = user_tuple[0] if user_tuple else None

    # Niet meerdere apparaten tot de dezelfde eigenaar toekenen dat werkt nog niet
    mycursor.execute("SELECT Name_Device FROM Device WHERE UserID = '{}'".format(user))
    device = mycursor.fetchone()

    if device != None:
        status = "#5db657"
    else:
        status = "#f9434e"    

    #usage(user, device, "HOUR")

    # print("What", chart(user, device, "HOUR")[0])

    #print(user, device)
    
    context = {
        'user': username,
        'device': device,
        'status': status,
        'hour': usage(user, device, "HOUR"),
        'day': usage(user, device, "DAY"),
        'month': usage(user, device, "MONTH"),
        'year': usage(user, device, "YEAR"),
        'date': chart(user, device, "HOUR")[0],
        'value': chart(user, device, "HOUR")[1],
    }

    #print(calculate_hourly_energy(device, "HOUR"))
            
    # print(type(context), context)

    # print("Context:", context, "\n")

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


# Data collection of the Raspberry Pi Pico
@csrf_exempt
def receive_data(request):
    #if request.method == "POST":
        #data = json.loads(request.body.decode('utf-8'))

    sql = "insert into wattage (DeviceID, Volt, ampere, pulldatetime) VALUES (1, 230, 15, NOW());"

    mycursor.execute(sql)
    mydb.commit()

    print("data added")

    return HttpResponse()