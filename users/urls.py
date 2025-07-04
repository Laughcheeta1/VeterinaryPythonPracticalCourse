from django.urls import path
from . import views

urlpatterns = [
    path("/", views.landing_page, name="users_landing_page"),
    path("all", views.all_users, name="all_users"),
    path("register", views.register_user, name="register_user"),
    path("one/<int:user_id>", views.particular_user, name="particular_user"),
    path("edit/<int:user_id>", views.edit_user, name="edit_user"),
    path("delete/<int:user_id>", views.delete_user, name="delete_user"),
    path("download", views.download_csv, name="download_users"),
]
