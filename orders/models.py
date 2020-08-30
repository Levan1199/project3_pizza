from django.db import models


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

class Order(models.Model):    
    regular_pizza = models.ManyToManyField(RegularPizza, blank=True, related_name="regular_pizza")
    sicilian_pizza = models.ManyToManyField(SicilianPizza, blank=True, related_name="sicilian_pizza")
    toppings = models.ManyToManyField(Toppings, blank=True, related_name="toppings")
    subs = models.ManyToManyField(Subs, blank=True, related_name="subs")
    salads = models.ManyToManyField(Salads, blank=True, related_name="salads")
    pasta = models.ManyToManyField(Pasta, blank=True, related_name="pasta")
    dinner_platters = models.ManyToManyField(DinnerPlatters, blank=True, related_name="dinner_platters")
