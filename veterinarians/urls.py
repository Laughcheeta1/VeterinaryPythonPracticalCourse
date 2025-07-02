from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="veterinarians_landing_page"),
    path("one/<int:veterinarian_id>", views.particular_veterinarian, name="particular_veterinarian"),
    path("download", views.download_csv, name="download_veterinarians"),
]
