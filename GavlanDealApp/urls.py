from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("last_deals", views.last_deals, name="last_deals"),
]