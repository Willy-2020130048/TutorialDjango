from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="item_home"),
    path("<int:item_id>", views.detail, name="item_detail"),
    path("delete/<int:item_id>", views.delete, name="item_delete"),

    path("request_view", views.requestView, name="request_view"),

    path('export', views.export_items, name='export_items'),


    path("vue", views.home_vue, name="vue_item_home"),
    path("vue/fetch", views.fetch_items, name="vue_item_fetch"),
    path("vue/<int:item_id>", views.detail, name="vue_item_detail"),
    path("vue/delete/<int:item_id>", views.delete, name="vue_item_delete"),
]