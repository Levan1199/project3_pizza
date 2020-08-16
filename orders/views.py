from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import RegularPizza

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

def menu(request):
    context = {
        "regular_pizza": RegularPizza.objects.all()
    }    
    return render(request, "pizzas/menu.html", context)