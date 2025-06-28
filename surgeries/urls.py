from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="surgeries_landing_page"),
    path("all", views.all_surgeries, name="all_surgeries"),
    path("register", views.register_surgery, name="register_surgery"),
    path("one/<int:surgery_id>", views.particular_surgery, name="particular_surgery"),
    path("edit/<int:surgery_id>", views.edit_surgery, name="edit_surgery"),
    path("delete/<int:surgery_id>", views.delete_surgery, name="delete_surgery")
]
