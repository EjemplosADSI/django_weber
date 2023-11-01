from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.management import call_command

def index(request):
    call_command('load_all')
    return HttpResponse("Export realizado.")
