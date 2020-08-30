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
<<<<<<< HEAD
#     contextJSON = dumps(context)
#     return render(request, 'pizzas/menu.html', {'data':contextJSON}) 


=======
#     # contextJSON = dumps(context)
#     return render(request, 'pizzas/menu.html', {'data':contextJSON}) 

>>>>>>> a100666f26cf2d6be4981ac9c27e80c2ccff7716
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
<<<<<<< HEAD
    }              
    return render(request, 'pizzas/menu.html', context)

=======
    }          
    
    return render(request, 'pizzas/menu.html', context)
>>>>>>> a100666f26cf2d6be4981ac9c27e80c2ccff7716

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

def order(request,pizza_type,pizza_name):
    quantity = int(request.POST["quantity"])
    size = str(request.POST["size"])    
    if pizza_type == "RegularPizza":
        pizza = RegularPizza.objects.get(name=pizza_name)
    if pizza_type == "SicilianPizza":
        pizza = SicilianPizza.objects.get(name=pizza_name)
    if pizza_type == "Toppings":
        pizza = Toppings.objects.get(name=pizza_name)
    if pizza_type == "Subs":
        pizza = Subs.objects.get(name=pizza_name)
    if pizza_type == "Salads":
        pizza = Salads.objects.get(name=pizza_name)
    if pizza_type == "Pasta":
        pizza = Pasta.objects.get(name=pizza_name)
    if pizza_type == "DinnerPlatters":
        pizza = DinnerPlatters.objects.get(name=pizza_name)

    print(quantity, size, pizza_name)
    print(pizza)

    return HttpResponseRedirect(reverse("menu"))
