# Was here before
from django.shortcuts import render
# Need it to return a simple response
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")