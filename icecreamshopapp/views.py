from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Icecreamshop

# Create your views here.

def index(request):
    myIcecreamshop = Icecreamshop.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myIcecreamshop': myIcecreamshop
    }
    return HttpResponse(template.render(context, request))

