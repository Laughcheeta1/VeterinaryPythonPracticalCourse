from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'users/users_landing.html', {})

def all_users(request):
    return render(request, 'users/users_landing.html', {})

def register_user(request):
    return render(request, 'users/users_landing.html', {})

def search_user(request):
    return render(request, 'users/users_landing.html', {})

def particular_user(request):
    return render(request, 'users/users_landing.html', {})
