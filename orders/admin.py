from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Subs, Salads, Toppings, DinnerPlatters, Pasta

# Register your models here.

admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Subs)
admin.site.register(Salads)
admin.site.register(Toppings)
admin.site.register(DinnerPlatters)
admin.site.register(Pasta)
