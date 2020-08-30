from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import RegularPizza, SicilianPizza, Toppings, Subs, Salads, Pasta, DinnerPlatters
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from json import dumps
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")

# def menu(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("index"))
#     context = {
#         "regular_pizza": serializers.serialize('json', RegularPizza.objects.all()),
#         "sicilian_pizza": serializers.serialize('json', SicilianPizza.objects.all()),
#         "toppings": serializers.serialize('json', Toppings.objects.all()),
#         "subs": serializers.serialize('json', Subs.objects.all()),
#         "salads": serializers.serialize('json', Salads.objects.all()),
#         "pasta": serializers.serialize('json', Pasta.objects.all()),
#         "dinner_platters": serializers.serialize('json', DinnerPlatters.objects.all()),
#     }          
#     # contextJSON = dumps(context)
#     return render(request, 'pizzas/menu.html', {'data':contextJSON}) 

def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    context = {
        "regular_pizza": RegularPizza.objects.all(),
        "sicilian_pizza": SicilianPizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "salads": Salads.objects.all(),
        "pasta": Pasta.objects.all(),
        "dinner_platters": DinnerPlatters.objects.all(),
    }          
    
    return render(request, 'pizzas/menu.html', context)

def login_view(request):
    print('inside reg log')
    username = str(request.POST["username"])
    password = str(request.POST["password"])
    user = authenticate(username=username, password=password)
    if user is not None:
        print('success')
        login(request,user)
        return HttpResponseRedirect(reverse("menu"))
    else:
        print('no success')
        return HttpResponseRedirect(reverse("index"))
    

def register(request):
    print('inside reg')
    username = str(request.POST["username"])
    password = str(request.POST["password"])    
    email = str(request.POST["email"])    
    user = User.objects.create_user(username,email,password)
    user.save()
    print("success")
    return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    print('inside out log')
    logout(request)
    return HttpResponseRedirect(reverse("index"))