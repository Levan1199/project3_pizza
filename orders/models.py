from django.db import models

# Create your models here.

class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.small_price} - {self.large_price}"

class SicilianPizza(models.Model,RegularPizza):
    pass
