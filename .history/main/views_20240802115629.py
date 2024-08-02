from django.shortcuts import render
from .models import *

def index(request):
    services = Services.objects.all()
    Portfolio
    context = {
        'services': services
    }
    return render(request,'services.html', context)