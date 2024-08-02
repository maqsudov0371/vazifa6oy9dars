from django.shortcuts import render
from .models import *

def index(request):
    services = Services.objects.all()
    return render(request,'services.html', context)
    context = {
        'services': services
    }