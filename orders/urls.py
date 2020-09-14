from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [    
    path("", views.index, name="index"),
    path("template_account", views.template_account, name="template_account"),
    path("menu", views.menu, name="menu"),    
    path("login_view", views.login_view, name="login"),
    path("logout_view", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<str:pizza_type>/<str:pizza_name>/order",views.order, name="order"),
    path("cart",views.cart, name="cart"),
    path("<str:pizza_type>/<int:pizza_pk>/remove",views.remove, name="remove"),
    path("payment", views.payment, name="payment")
]
