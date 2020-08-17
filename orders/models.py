from django.db import models

# Create your models here.

class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.small_price} - {self.large_price}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.small_price} - {self.large_price}"

class Toppings(models.Model):
    name = models.CharField(max_length=64)    

    def __str__(self):
        return f"{self.name}"

class Subs(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.small_price} - {self.large_price}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()   

    def __str__(self):
        return f"{self.name} - {self.price}"

class Salads(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()   

    def __str__(self):
        return f"{self.name} - {self.price}"

class DinnerPlatters(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.small_price} - {self.large_price}"