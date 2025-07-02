from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="appointments_landing_page"),
    path("all", views.all_appointments, name="all_appointments"),
    path("register", views.register_appointment, name="register_appointment"),
    path("register/<int:pet_id>", views.register_appointment, name="register_appointment"),
    path("one/<int:appointment_id>", views.particular_appointment, name="particular_appointment"),
    path("edit/<int:appointment_id>", views.edit_appointment, name="edit_appointment"),
    path("delete/<int:appointment_id>", views.delete_appointment, name="delete_appointment"),
    path("download", views.download_csv, name="download_appointments"),

    # For the annotation
    path('<int:appointment_id>/annotations/', views.all_annotations, name="annotations_appointment"),
    path('<int:appointment_id>/annotation/register', views.register_annotation, name="register_annotation"),
    path('<int:appointment_id>/annotation/<int:annotation_id>', views.particular_annotation, name="particular_annotation"),
    path('<int:appointment_id>/annotation/<int:annotation_id>/edit', views.edit_annotation, name="edit_annotation"),
    path('<int:appointment_id>/annotation/<int:annotation_id>/delete', views.delete_annotation, name="delete_annotation"),
]
