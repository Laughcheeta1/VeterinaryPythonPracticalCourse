from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def landing_page(request):
    return render(request, 'users/users_landing.html', {})


def all_users(request):
    users = User.objects.all()

    context = { 
        'objects' : users,
        'page_name' : 'All Users',
        'base_url' : 'particular_user'
    }

    return render(request, 'common/all.html', context)


def register_user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Usuario Exitoso',
                'return_page_name' : 'Users',
                'desired_url' : 'users_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar el usuario',
                'return_page_name' : 'Users',
                'desired_url' : 'users_landing_page'
            }
            return render(request, 'common/result_page.html', context)

    context = { 'form': form }
    return render(request, 'users/register_user.html', context)


def edit_user(request, user_id):
    try:
        desired_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        context = {
            'message': 'the desired user does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Usuario Exitoso',
                'return_page_name' : 'Users',
                'desired_url' : 'users_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar el usuario',
                'return_page_name' : 'Users',
                'desired_url' : 'users_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        
    
    form = UserForm(instance=desired_user)

    context = { 
        'page_name' : 'Edit User',
        'object': desired_user,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def search_user(request):
    return render(request, 'users/users_landing.html', {})


def particular_user(request, user_id):
    try:
        desired_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        context = {
            'message': 'the desired user does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'User',
        'object': desired_user,
        'edit_url' : 'edit_user',
    }

    return render(request, 'common/particular.html', context)
