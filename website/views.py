# Import Django libraries
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.core.serializers.json import DjangoJSONEncoder

# Import non-Django libraries
from datetime import datetime, timedelta
from coolname import generate_slug
from threading import Thread

import mysql.connector
import json
import queue
import time
import os

# Import other python files
from .connect import *
from .math import *
from website.settings import Settings
from .pico import PicoReader

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="energy_guardian",
    port=3306,
)

mycursor = connection.cursor()

database = connecter()

pico_reader = PicoReader()

def read_pico_data():
    time.sleep(1)
    while True:
        data_to_send = "True"
        
        pico_reader.send_signal(data_to_send + "\n")

        data = pico_reader.read_data()

        try:

            print("Data:", type(data), data)

            data = data.split(',')

            DeviceID, Voltage, Current = data

            sql = "SELECT WattageID FROM wattage WHERE DeviceID = %s"

            mycursor.execute(sql, (DeviceID,))
            wattageID = [row[0] for row in mycursor.fetchall()]

            old = 0
            wID= 0
            through = True
            
            for id in wattageID:
                if id == old:
                    old +=1
                else:
                    wID = old
                    through = False
                    break

            if through:
                while wID in wattageID:
                    wID += 1

            sql = "INSERT INTO wattage (WattageID, DeviceID, Volt, Ampere, pulldatetime) VALUES (%s, %s, %s, %s, NOW())"

            val = (wID, DeviceID, Voltage, Current)

            try:
                mycursor.execute(sql, val)
                connection.commit()
                print("Data added to database.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

        except ValueError:
            print("Error:", type(data), data)

        time.sleep(1)
            
    print("test")


# thread = Thread(target=read_pico_data)
# thread.daemon = True
# thread.start()

#Home pagina
def home(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


# Login pagina
@csrf_protect
def login(request):
    # mydbLogin = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="toor",
    #     database="energy_guardian",
    #     port=3306,
    # )
    
    # mycursorLogin = mydbLogin.cursor()

    try:
        user = request.session["user"]
        return redirect('dashboard')
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

        # Het uitvoeren van de query met de opgehaalde gegevens
        mycursor.execute("SELECT * FROM users WHERE email_address = %s", (email,))

        myresult = mycursor.fetchall()
        print(myresult)
        
        #decrpytie

        for x in myresult:
            # Checken of het de juiste gegevens zijn
            if (x[1] == email and B.checkpw(password.encode('utf-8'), x[4].encode('utf-8'))):
                print("Succes")
                request.session["user"] = x[0]
                response = redirect("dashboard")
                return response
            
            else:
                print("ERROR NERD")

    return render(request, "login.html")


# dashboard page with dashboard
def dashboard(request):
    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')

    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    username = user_tuple[0] if user_tuple else None

    time.sleep(0.1)

    # Niet meerdere apparaten tot de dezelfde eigenaar toekenen dat werkt nog niet
    mycursor.execute("SELECT Name_Device FROM Device WHERE UserID = '{}'".format(user))
    device = mycursor.fetchone()

    if device_status(user):
        status = "#5db657"
    else:
        status = "#f9434e"
    
    context = {
        'user': username,
        'device': device,
        'status': status,
        'hour': usage(user, device, "HOUR"),
        'day': usage(user, device, "DAY"),
        'week': usage(user, device, "WEEK"),
        'month': usage(user, device, "MONTH"),
        'year': usage(user, device, "YEAR"),
        'date': chart(user, device, "HOUR")[0],
        'value': chart(user, device, "HOUR")[1],
    }

    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context, request))


# Plotter pagina
def plotter(request):
    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')

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
    
    return redirect("dashboard")


# Signup pagina maken
def signup(request):
    try:
        user = request.session["user"]
        return redirect('dashboard')
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


def settings(request):
    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')

    if request.method == "POST":
        change = Settings()
        
        password1 = request.POST.get("password")
        password2 = request.POST.get("passwordRepeat")
        
        if password1 != None:
            if (password1 == password2) and password1 !="" and password2 != "": 
                change.changePassword(user, password1)        
        else:
            change.deleteAccount(user)
            del request.session["user"]
            return render(request, 'index.html')

    return render(request, 'settings.html')

# Page to register a device
@csrf_protect
def register(request):
    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')
    
    if request.method == 'POST':

        number = request.POST.get("device-Name")

        pico_reader.register(number, user)
    
    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    username = user_tuple[0] if user_tuple else None

    mycursor.execute("SELECT * FROM Device where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    device = user_tuple[0] if user_tuple else None

    context = {
        'user': username,
        'device': 2,
    }

    template = loader.get_template("register.html")
    return HttpResponse(template.render(context, request))