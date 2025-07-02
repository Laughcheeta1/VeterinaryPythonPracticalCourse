from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="pets_landing_page"),
    path("all", views.all_pets, name="all_pets"),
    path("register", views.register_pet, name="register_pet"),
    path("one/<int:pet_id>", views.particular_pet, name="particular_pet"),
    path("edit/<int:pet_id>", views.edit_pet, name="edit_pet"),
    path("delete/<int:pet_id>", views.delete_pet, name="delete_pet"),
    path("medic_history/<int:pet_id>", views.medic_history, name="medic_history"),
    path("download", views.download_csv, name="download_pets"),
]
