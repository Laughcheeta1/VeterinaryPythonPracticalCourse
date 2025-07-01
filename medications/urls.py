from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="medications_landing_page"),
    path("all", views.all_medications, name="all_medications"),
    path("register", views.register_medication, name="register_medication"),
    path("one/<int:medication_id>", views.particular_medication, name="particular_medication"),
    path("edit/<int:medication_id>", views.edit_medication, name="edit_medication"),
    path("delete/<int:medication_id>", views.delete_medication, name="delete_medication")
]
