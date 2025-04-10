from django.shortcuts import render

# Create your views here.
# meu_app/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Primeira página Django.")
