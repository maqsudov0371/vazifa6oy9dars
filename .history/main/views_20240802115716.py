from django.shortcuts import render
from .models import *

def index(request):
    services = Services.objects.all()
    portfolios = Portfolio.objects.all()
    about = About.objects.all()
    context = {
        'services': services,
        'portfolios': portfolios,
        'about': about,
    }
    return render(request,'ind.html', context)