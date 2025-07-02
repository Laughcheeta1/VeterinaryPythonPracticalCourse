from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="medications_landing_page"),
    path("one/<int:medication_id>", views.particular_medication, name="particular_medication"),
    path("download", views.download_csv, name="download_medications"),
]
