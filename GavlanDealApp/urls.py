from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("last_deals", views.last_deals, name="last_deals"),
    path("add_deal", views.add_deal, name="add_deal"),
    path("generate_qr", views.generate_qr, name="generate_qr"),
    path("product", views.product, name="product"),
    path("product_list", views.product_list, name="product_list"),
]