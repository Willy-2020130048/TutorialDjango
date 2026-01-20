from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="customer_home"),
    path("add", views.add, name="customer_add"),
    path("<int:customer_id>", views.detail, name="customer_detail"),
    path("delete/<int:customer_id>", views.delete, name="customer_delete"),

    path("vue", views.home, name="vue_customer_home"),
    path("vue/add", views.add, name="vue_customer_add"),
    path("vue/<int:customer_id>", views.detail, name="vue_customer_detail"),
    path("vue/delete/<int:customer_id>", views.delete, name="vue_customer_delete"),
]