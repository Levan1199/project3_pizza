from django.db import models
from django.conf import settings

# Create your models here.

class RegularPizza(models.Model):
    pizza_type = models.CharField(max_length=64,default="RegularPizza")
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.pizza_type} - {self.name} - {self.small_price} - {self.large_price}"

class SicilianPizza(models.Model):
    pizza_type = models.CharField(max_length=64,default="SicilianPizza")
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.pizza_type} - {self.name} - {self.small_price} - {self.large_price}"

class Toppings(models.Model):
    pizza_type = models.CharField(max_length=64,default="Toppings")
    name = models.CharField(max_length=64)    

    def __str__(self):
        return f"{self.pizza_type} - {self.name}"

class Subs(models.Model):
    pizza_type = models.CharField(max_length=64,default="Subs")
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.pizza_type} - {self.name} - {self.small_price} - {self.large_price}"

class Pasta(models.Model):
    pizza_type = models.CharField(max_length=64,default="Pasta")
    name = models.CharField(max_length=64)
    price = models.FloatField()   

    def __str__(self):
        return f"{self.pizza_type} - {self.name} - {self.price}"

class Salads(models.Model):
    pizza_type = models.CharField(max_length=64,default="Salads")
    name = models.CharField(max_length=64)
    price = models.FloatField()   

    def __str__(self):
        return f"{self.pizza_type} - {self.name} - {self.price}"

class DinnerPlatters(models.Model):
    pizza_type = models.CharField(max_length=64,default="DinnerPlatters")
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.pizza_type} - {self.name} - {self.small_price} - {self.large_price}"

# class Order(models.Model):        
#     regular_pizza = models.ManyToManyField(RegularPizza, blank=True, related_name="regular_pizza")
#     sicilian_pizza = models.ManyToManyField(SicilianPizza, blank=True, related_name="sicilian_pizza")
#     toppings = models.ManyToManyField(Toppings, blank=True, related_name="toppings")
#     subs = models.ManyToManyField(Subs, blank=True, related_name="subs")
#     salads = models.ManyToManyField(Salads, blank=True, related_name="salads")
#     pasta = models.ManyToManyField(Pasta, blank=True, related_name="pasta")
#     dinner_platters = models.ManyToManyField(DinnerPlatters, blank=True, related_name="dinner_platters")

#     def __str__(self):
#         return f"{self.pk}"

# class Order(models.Model):
#     pass


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE ,related_name="user_cart")
    # order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="cart")
    

    def __str__(self):
        return f"{self.pk} - {self.user}"


class RegularPizzaOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="reg_order")
    dish = models.ForeignKey(RegularPizza, on_delete=models.CASCADE, related_name="regular_pizza")
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=64,default="Small")

    def __str__(self):
        return f"{self.cart} - {self.quantity} - {self.size}"


class SicilianPizzaOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="sic_order")
    dish = models.ForeignKey(SicilianPizza, on_delete=models.CASCADE, related_name="sicilian_pizza")
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=64,default="Small")

    def __str__(self):
        return f"{self.cart} - {self.quantity} - {self.size}"

class ToppingsOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="top_order")
    dish = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="toppings")
    # quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.cart} "

class SubsOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="sub_order")
    dish = models.ForeignKey(Subs, on_delete=models.CASCADE, related_name="subs")
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=64,default="Small")
    
    def __str__(self):
        return f"{self.cart} - {self.quantity} - {self.size}"

class PastaOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="pas_order")
    dish = models.ForeignKey(Pasta, on_delete=models.CASCADE, related_name="pasta")
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.cart} - {self.quantity} "

class SaladsOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="sal_order")
    dish = models.ForeignKey(Salads, on_delete=models.CASCADE, related_name="salads")
    quantity = models.IntegerField(default=1)   
    
    def __str__(self):
        return f"{self.cart} - {self.quantity} "

class DinnerPlattersOrder(models.Model):    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_of_cart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="din_order")
    dish = models.ForeignKey(DinnerPlatters, on_delete=models.CASCADE, related_name="dinner_platters")
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=64,default="Small")
    
    def __str__(self):
        return f"{self.cart} - {self.quantity} - {self.size}"