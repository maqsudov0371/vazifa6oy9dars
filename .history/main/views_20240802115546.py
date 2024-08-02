from django.shortcuts import render
from .models import *

def index(request):
    services = Services.objects.all()
    context = [
        'services'
    ]