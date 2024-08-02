from django.shortcuts import render
from .models import *

def index(request):
    services = Services.objects.all()
    portfolios = Portfolio.objects.all()
    about = 
    context = {
        'services': services
    }
    return render(request,'services.html', context)