from django.http import HttpResponse
from django.template import loader
from .models import Wattage

def login(request):
    data = Wattage.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())