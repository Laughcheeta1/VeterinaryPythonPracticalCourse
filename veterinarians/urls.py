from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="veterinarians_landing_page"),
    path("all", views.all_veterinarians, name="all_veterinarians"),
    path("register", views.register_veterinarian, name="register_veterinarian"),
    path("one/<int:veterinarian_id>", views.particular_veterinarian, name="particular_veterinarian"),
    path("edit/<int:veterinarian_id>", views.edit_veterinarian, name="edit_veterinarian"),
    path("delete/<int:veterinarian_id>", views.delete_veterinarian, name="delete_veterinarian")
]
