from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="appointments_landing_page"),
    path("all", views.all_appointments, name="all_appointments"),
    path("register", views.register_appointment, name="register_appointment"),
    path("one/<int:appointment_id>", views.particular_appointment, name="particular_appointment"),
    path("edit/<int:appointment_id>", views.edit_appointment, name="edit_appointment"),
    path("delete/<int:appointment_id>", views.delete_appointment, name="delete_appointment")
]
