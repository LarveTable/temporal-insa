# Was here before
from django.shortcuts import render

# Create your views here.
# Ici c'est la page d'acceuil
def index(request):
    return render(request, "webapp/home.html")

# Ici page de creation d'expérience
def new(request):
    return render(request, "webapp/new.html")

# Ici page de classification
def classify(request):
    return render(request, "webapp/classify.html")