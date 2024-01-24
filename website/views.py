# Import Django libraries
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.core.serializers.json import DjangoJSONEncoder

# Import non-Django libraries
from kaspersmicrobit.bluetoothprofile.services import Service
from kaspersmicrobit import KaspersMicrobit
from datetime import datetime, timedelta
from coolname import generate_slug
from threading import Thread

import mysql.connector
import json
import queue
import time
import os
import threading
import concurrent.futures

# Import other python files
from .connect import *
from .math import *
from website.settings import Settings
from .pico import PicoReader

database = connecter()

pico_reader = PicoReader()

pause_event = threading.Event()

def microbit():
    def pressed(button):
        time.sleep(0.1)

    def pressed_long(button):
        time.sleep(0.1)

    def released(button):
        if button == "A":
            pico_reader.send_signal("off" + "\n")
            time.sleep(1)
            print("Device is turned off.")
        
        if button == "B":
            pico_reader.send_signal("on" + "\n")
            time.sleep(1)
            print("Device is turned on.")

        # print(f"button {button} released")
            
    while True:
        try:
            with KaspersMicrobit('DC:85:FE:2B:CB:D8') as microbit:
                print(f'Bluetooth address: {microbit.address()}')
                print(f"Device name: {microbit.generic_access.read_device_name()}")
                
                # read the state of the buttons / lees de toestant van de knoppen
                # print(f"button A state is now: {microbit.buttons.read_button_a()}")
                # print(f"button B state is now: {microbit.buttons.read_button_b()}")

                # listen for button events / luister naar drukken op knoppen
                microbit.buttons.on_button_a(press=pressed, long_press=pressed_long, release=released)
                microbit.buttons.on_button_b(press=pressed, long_press=pressed_long, release=released)

                time.sleep(15)
        except Exception:
            time.sleep(1)

def read_pico_data():
    time.sleep(1)
    while True:
        while not pause_event.is_set():
            pico_reader.send_signal("True" + "\n")

            # Database connection
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="toor",
                database="energy_guardian",
                port=3306,
            )

            mycursor = connection.cursor()

            try:
                try:
                    data = pico_reader.read_data()

                    print("Data:", data)

                    data = data.split(',')

                    DeviceID, Voltage, Current = data

                    Watt = float(Voltage) * float(Current)

                    try:
                        sql = "SELECT Average_Voltage, Average_Ampere FROM calibration WHERE DeviceID = %s"
                        mycursor.execute(sql, (DeviceID,))
                        Data = mycursor.fetchall()[0]

                        Average_Watt = float(Data[0]) * float(Data[1])

                        # print(Average_Watt)

                        if abs(Watt - Average_Watt) <= 0.2:
                            pico_reader.send_signal("off" + "\n")

                    except IndexError:
                        time.sleep(0.1)

                    sql = "SELECT WattageID FROM wattage"
                    mycursor.execute(sql)
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
                        # print("Data added to database.\n")
                    except mysql.connector.Error as err:
                        print(f"Error: {err}\n")
                except AttributeError:
                    time.sleep(1)
            except ValueError or AttributeError:
                print("Error:", type(data), data)

            time.sleep(2)

# Start the necessary threads for the Pico and the Micro:bit.
thread = Thread(target=read_pico_data, daemon=True)
thread.start()

thread2 = Thread(target=microbit, daemon=True)
thread2.start()

#Home pagina
def home(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


# Login pagina
@csrf_protect
def login(request):
    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="energy_guardian",
        port=3306,
    )

    mycursor = connection.cursor()

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
        
        if myresult == []:
            return render(request, "login.html", {'Invalid':True})
        #decrpytie

        for x in myresult:
            # Checken of het de juiste gegevens zijn
            if (x[1] == email and B.checkpw(password.encode('utf-8'), x[4].encode('utf-8'))):
                print("Succes")
                request.session["user"] = x[0]
                response = redirect("dashboard")
                return response
            
            else:
                return render(request, "login.html", {'login_error':True})

    return render(request, "login.html")


# dashboard page with dashboard
def dashboard(request):
    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="energy_guardian",
        port=3306,
    )

    mycursor = connection.cursor()

    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')

    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchall()    

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
        'user': username[0],
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
    
    failed = False  # Initialize here

    if request.method == 'POST':
        database = connecter()
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("secondName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordRepeat = request.POST.get("passwordRepeat")
        
        if password != passwordRepeat:
            return render(request, 'signUp.html', {'passwordFail': True})
        
        signup = database.signUp(email, firstName, lastName, password)

        if signup == "Empty":
            pass
        
        elif signup == "PasswordError":
            return render(request, 'signUp.html', {'password_failed': True})
        
        elif signup == "toLongFirst":
            return render(request, 'signUp.html', {'toLongFirst': True})
        
        elif signup == "toLongLast":
            return render(request, 'signUp.html', {'toLongLast': True})
        
        elif signup == "toLongEmail":
            return render(request, 'signUp.html', {'toLongEmail': True})
        
        elif signup == "toShortPassword":
            return render(request, 'signUp.html', {'toShortPassword': True})
        
        elif signup == "toLongPassword":
            return render(request, 'signUp.html', {'toLongPassword': True})
        
        elif signup == "emailError":
            return render(request, 'signUp.html', {'create_user_failed': failed})
            
        else:
            return redirect("login")
    
    return render(request, 'signUp.html')

#Settings 
def settings(request):
    user = request.session["user"]
    
    if user is None:
        return redirect ("accountDeleted")
    
    if request.method == "POST":
        change = Settings()
        
        password1 = request.POST.get("password")
        password2 = request.POST.get("passwordRepeat")
        
        if password1 != None:
            print("IN")
            print(password1, password2)
            if password1 == password2: 
                if(change.changePassword(user, password1)):
                    print("Changed")
                
                else:
                    return render(request, 'settings.html', {'passwordError':True})
            
        
        else:
            change.deleteAccount(user)
            del request.session["user"]
            return redirect ("accountDeleted")

    return render(request, 'settings.html')        

def delete(request):
    user = request.session.get("user")
    if user is None:
        return render(request, 'accountDeleted.html', {"deleted_account":True})

# Page to register a device
@csrf_protect
def register(request):
    """
        1. Verbind het apparaat
        2. Registreren of stap 3
        3. Kalibreren.
            Wanneer op de knop aan of uit gedrukt wordt:
                a. Functie read_pico_data stoppen, zodat er geen conflict ontstaat.
                b. "True" verzenden naar de Pico, zodat deze data gaat verzenden.
                c. Data lezen en opslitsen in de juiste variabelen.
                d. device += 1

    """

    # Database connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="energy_guardian",
        port=3306,
    )

    mycursor = connection.cursor()

    try:
        user = request.session["user"]
    except KeyError:
        return redirect('login')
    
    device = 0        
    
    mycursor.execute("SELECT FirstName FROM users where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    username = user_tuple[0] if user_tuple else None

    mycursor.execute("SELECT * FROM Device where UserID = '{}'".format(user))
    user_tuple = mycursor.fetchone()    

    device = user_tuple[0] if user_tuple else None

    if request.method == 'POST':

        number = request.POST.get("device-Name")
        # aan = request.POST.get("aan")
        uit = request.POST.get("uit")

        if number != None:
            print("Registering device.")
            pico_reader.register(number, user)
        else:
            # Get the deviceid out of the database
            sql = "SELECT DeviceID FROM device WHERE UserID = %s;"
            mycursor.execute(sql, (user,))
            number = mycursor.fetchone()[0]

        # if aan != None:
        #     print("Aan")
        #     pause_event.set()
        #     pico_reader.calibration(number, 1)
        #     device = 0

        if uit != None:
            print("Uit")
            pause_event.set()
            pico_reader.calibration(number, 0)
            device = 1

        # print(device)

    context = {
        'user': username,
        'device': device,
    }

    return render(request, "register.html", context)

def update(request):
    return render(request, "update.html")