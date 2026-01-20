from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="item_home"),
    path("<int:item_id>", views.detail, name="item_detail"),
    path("delete/<int:item_id>", views.delete, name="item_delete"),

    path("vue", views.home, name="vue_item_home"),
    path("vue/fetch", views.fetch_items, name="vue_item_fetch"),
    path("vue/<int:item_id>", views.detail, name="vue_item_detail"),
    path("vue/delete/<int:item_id>", views.delete, name="vue_item_delete"),
]