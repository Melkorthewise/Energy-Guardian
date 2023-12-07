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
    #username = request.POST.get['username']
    #password = request.POST.get['password']

    #for p in Login.objects.raw("SELECT * FROM login"):
    #    print(p)

    if request.method == "POST":
        #current_user_profile = request.user.profile
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)
    
        # mycursor.execute("SELECT * FROM login WHERE username")

        # myresult = mycursor.fetchall()

        # for x in myresult:
        #     print(x)

    return render(request, "login.html")


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def home(request):
    return render(request, "index.html")