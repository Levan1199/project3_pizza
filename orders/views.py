from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import RegularPizza, SicilianPizza, Toppings, Subs, Salads, Pasta, DinnerPlatters, Cart
from .models import RegularPizzaOrder, SicilianPizzaOrder, ToppingsOrder, SubsOrder, SaladsOrder, DinnerPlattersOrder, PastaOrder
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from json import dumps
from django.core import serializers

# Create your views here.

def index(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("menu"))
    # else:
    return render(request, "theme/index.html")

def template_account(request):
    if request.user.is_authenticated:
        us_name = request.user.username
        us = User.objects.get(username=us_name)
        return render(request, "theme/account2.html", {'user':us})
    else:
        return render(request, "theme/account.html")
    

def menu(request):
    context = {        
        "username": request.user.username,
        "regular_pizza": RegularPizza.objects.all(),
        "sicilian_pizza": SicilianPizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "salads": Salads.objects.all(),
        "pasta": Pasta.objects.all(),
        "dinner_platters": DinnerPlatters.objects.all(),
    }                  
    return render(request, 'theme/menu.html', context)


def login_view(request):
    username = str(request.POST["username"])
    password = str(request.POST["password"])
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("menu"))
    else:
        return HttpResponseRedirect(reverse("index"))
    

def register(request):
    username = str(request.POST["username"])
    password = str(request.POST["password"])    
    email = str(request.POST["email"])    
    user = User.objects.create_user(username,email,password)
    user.save()
    return HttpResponseRedirect(reverse("menu"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def order(request,pizza_type,pizza_name): 
    try:
        us_name = request.user.username
        user = User.objects.get(username=us_name)    
    except:
        return render(request, 'theme/error.html',{'message': 'You need to log in first'})
    
    try:
        quantity = int(request.POST["quantity"])
        size = str(request.POST["size"])
    except:
        pass
  
    try:
        cart = Cart.objects.get(user=user)       
    except Cart.DoesNotExist:        
        cart = Cart.objects.create(user=user)        
        cart.save()
    
   ###  so luong
    if pizza_type == "RegularPizza":
        pizza = RegularPizza.objects.get(name=pizza_name)       
        ordered_pizza = RegularPizzaOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:   
                    if one.size == size:                        
                        quantity += one.quantity       
                        one.quantity = quantity # increase quantity                    
                        one.save()
                        added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                RegularPizzaOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size) 
        else:
            # No orders before
            RegularPizzaOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size)         
    elif pizza_type == "SicilianPizza":
        pizza = SicilianPizza.objects.get(name=pizza_name)       
        ordered_pizza = SicilianPizzaOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:                             
                    if one.size == size:                        
                        quantity += one.quantity       
                        one.quantity = quantity # increase quantity                    
                        one.save()
                        added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                SicilianPizzaOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size) 
        else:
            # No orders before
            SicilianPizzaOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size)   

    elif pizza_type == "Toppings":       
        pizza = Toppings.objects.get(name=pizza_name)       
        ordered_pizza = ToppingsOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:                                
                    added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                ToppingsOrder.objects.create(cart=cart,dish=pizza) 
        else:
            # No orders before
            ToppingsOrder.objects.create(cart=cart,dish=pizza)  
        
    elif pizza_type == "Subs":
        pizza = Subs.objects.get(name=pizza_name)       
        ordered_pizza = SubsOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:                               
                    if one.size == size:                        
                        quantity += one.quantity       
                        one.quantity = quantity # increase quantity                    
                        one.save()
                        added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                SubsOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size) 
        else:
            # No orders before
            SubsOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size)   
    elif pizza_type == "Salads":
        pizza = Salads.objects.get(name=pizza_name)       
        ordered_pizza = SaladsOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:                               
                    # if one.size == size:                        
                    quantity += one.quantity       
                    one.quantity = quantity # increase quantity                    
                    one.save()
                    added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                SaladsOrder.objects.create(cart=cart,dish=pizza,quantity=quantity) 
        else:
            # No orders before
            SaladsOrder.objects.create(cart=cart,dish=pizza,quantity=quantity)   
    elif pizza_type == "Pasta":
        pizza = Pasta.objects.get(name=pizza_name)       
        ordered_pizza = PastaOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:                                
                    # if one.size == size:                        
                    quantity += one.quantity       
                    one.quantity = quantity # increase quantity                    
                    one.save()
                    added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                PastaOrder.objects.create(cart=cart,dish=pizza,quantity=quantity) 
        else:
            # No orders before
            PastaOrder.objects.create(cart=cart,dish=pizza,quantity=quantity)  
    elif pizza_type == "DinnerPlatters":
        pizza = DinnerPlatters.objects.get(name=pizza_name)       
        ordered_pizza = DinnerPlattersOrder.objects.filter(dish = pizza)
        if ordered_pizza:            
            added_pizza = False
            for one in ordered_pizza:
                if one.dish == pizza and one.cart == cart:                             
                    if one.size == size:                        
                        quantity += one.quantity       
                        one.quantity = quantity # increase quantity                    
                        one.save()
                        added_pizza = True # Done increase the quantity               
            if not added_pizza:
                # Couldn't find the same pizza
                DinnerPlattersOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size) 
        else:
            # No orders before
            DinnerPlattersOrder.objects.create(cart=cart,dish=pizza,quantity=quantity,size=size)   
    return HttpResponseRedirect(reverse("menu"))

def cart(request):      
    total = 0
    try:
        us_name = request.user.username
        us = User.objects.get(username=us_name) ########
    except:
        return render(request, 'theme/cart.html')
    try:
        cart = Cart.objects.get(user=us)                
    except Cart.DoesNotExist:
        return render(request, 'theme/cart.html')
    for order in cart.reg_order.all():
        if order.size == "Small":
            total += order.dish.small_price * order.quantity          
        else:
            total += order.dish.large_price * order.quantity
    for order in cart.sic_order.all():
        if order.size == "Small":
            total += order.dish.small_price * order.quantity          
        else:
            total += order.dish.large_price * order.quantity
    for order in cart.sub_order.all():        
        if order.size == "Small":
            total += order.dish.small_price * order.quantity          
        else:
            total += order.dish.large_price * order.quantity        
    for order in cart.sal_order.all():    
        total += order.dish.price * order.quantity
    for order in cart.pas_order.all():     
        total += order.dish.price * order.quantity
    for order in cart.din_order.all():        
        if order.size == "Small":
            total += order.dish.small_price * order.quantity          
        else:
            total += order.dish.large_price * order.quantity
    context = {
        "total": total,
        "regular_pizza": cart.reg_order.all(),
        "sicilian_pizza": cart.sic_order.all(),
        "toppings": cart.top_order.all(),
        "subs": cart.sub_order.all(),
        "salads": cart.sal_order.all(),
        "pasta": cart.pas_order.all(),
        "dinner_platters": cart.din_order.all(),
    }              
    return render(request, 'theme/cart.html', context)

def remove(request,pizza_type,pizza_pk):
    if pizza_type == "RegularPizza":      
        pizza = RegularPizzaOrder.objects.get(pk=pizza_pk)         
        pizza.delete()        
    elif pizza_type == "SicilianPizza":
        pizza = SicilianPizzaOrder.objects.get(pk=pizza_pk)         
        pizza.delete()  
    elif pizza_type == "Toppings":
        pizza = ToppingsOrder.objects.get(pk=pizza_pk)         
        pizza.delete()    
    elif pizza_type == "Subs":
        pizza = SubsOrder.objects.get(pk=pizza_pk)         
        pizza.delete()    
    elif pizza_type == "Salads":
        pizza = SaladsOrder.objects.get(pk=pizza_pk)         
        pizza.delete()   
    elif pizza_type == "Pasta":
        pizza = PastaOrder.objects.get(pk=pizza_pk)         
        pizza.delete()  
    elif pizza_type == "DinnerPlatters":
        pizza = DinnerPlattersOrder.objects.get(pk=pizza_pk)         
        pizza.delete()     
    return HttpResponseRedirect(reverse("cart"))

def payment(request):
    us_name = request.user.username
    us = User.objects.get(username=us_name)
    try:
        cart = Cart.objects.get(user=us)  
    except:
        return render(request, 'theme/error.html',{'message':'No items to order'})
    cart.delete()
    return HttpResponseRedirect(reverse("cart"))