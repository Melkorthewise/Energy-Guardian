from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
#from .models import Wattage, Login
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie


@csrf_protect
def login(request):
    #username = request.POST['username']
    #password = request.POST['password']

    #for p in Login.objects.raw("SELECT * FROM login"):
    #    print(p)

    return render(request, "login.html")


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def home(request):
    return render(request, "index.html")