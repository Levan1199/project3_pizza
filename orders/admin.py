from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Subs, Salads, Toppings, DinnerPlatters, Pasta, Order, Cart
from .models import RegularPizzaOrder, SicilianPizzaOrder, SubsOrder, SaladsOrder, ToppingsOrder, DinnerPlattersOrder, PastaOrder
# class OrderInline(admin.StackedInline):
#     model = Order.regular_pizza.through
#     extra = 1

# class RegularPizzaAdmin(admin.ModelAdmin):
#     inlines = [OrderInline]

# class OrderAdmin(admin.ModelAdmin):
#     filter_horizontal = ("regular_pizza",
#                         "sicilian_pizza",
#                         "toppings",
#                         "subs",
#                         "salads",
#                         "pasta",
#                         "dinner_platters",                        
#                         )

# class RegCartAdmin(admin.ModelAdmin):
#     filter_horizontal = ("regular_pizza",
                        
#                         )

# Register your models here.

admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Subs)
admin.site.register(Salads)
admin.site.register(Toppings)
admin.site.register(DinnerPlatters)
admin.site.register(Pasta)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(RegularPizzaOrder)
admin.site.register(SicilianPizzaOrder)
admin.site.register(SubsOrder)
admin.site.register(SaladsOrder)
admin.site.register(ToppingsOrder)
admin.site.register(DinnerPlattersOrder)
admin.site.register(PastaOrder)