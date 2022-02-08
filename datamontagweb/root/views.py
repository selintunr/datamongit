from django.shortcuts import render
from django.http import HttpResponseRedirect

import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def indexen(request):
    return render(request, 'index-en.html')    


def member(request):
    return render(request, 'member.html')        