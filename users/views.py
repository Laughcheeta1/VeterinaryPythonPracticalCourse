from django.shortcuts import render
from .models import User

# Create your views here.
def landing_page(request):
    return render(request, 'users/users_landing.html', {})

def all_users(request):
    users = User.objects.all()

    context = { 'users' : users }

    return render(request, 'users/all_users.html', context)

def register_user(request):
    return render(request, 'users/users_landing.html', {})

def search_user(request):
    return render(request, 'users/users_landing.html', {})

def particular_user(request):
    return render(request, 'users/users_landing.html', {})
