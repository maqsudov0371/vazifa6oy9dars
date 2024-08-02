from django.shortcuts import render
from .models import *

def index(request):
    services = Services.objects.all()
    por
    context = {
        'services': services
    }
    return render(request,'services.html', context)