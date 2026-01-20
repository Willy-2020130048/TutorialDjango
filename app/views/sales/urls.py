from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="sales_home"),
    path("fetch", views.fetch_data, name="sales_fetch"),

    path("delete/<int:sales_id>", views.delete, name="sales_delete"),
]