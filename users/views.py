from django.shortcuts import render
from .models import User
from .forms import UserForm

# Create your views here.
def landing_page(request):
    context = {
        'page_name' : 'Users',
	    'object_name' : 'user',
	    'all_url' : 'all_users',
	    'register_url' : 'register_user',
	    'desired_image_url' : 'users/images/WomenHoldingPet.png',
	    'image_alt_name' :  'Woman holding golder retriever',
    }
    return render(request, 'common/landing.html', context)


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

    context = { 
        'form': form,
        'page_name' : 'Register User'
    }
    return render(request, 'common/register.html', context)


def edit_user(request, user_id):
    try:
        desired_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        context = {
            'message': 'the desired user does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=desired_user)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Actualizacion De Usuario Exitoso',
                'return_page_name' : 'Users',
                'desired_url' : 'users_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible actualizar el usuario',
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


def delete_user(request, user_id):
    try:
        desired_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        context = {
            'message': 'the desired user does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)
    
    desired_user.delete()
    context = {
        'message': 'El usuario fue eliminado exitosamente',
        'return_page_name' : 'Users',
        'desired_url' : 'users_landing_page'
    }
    return render(request, 'common/result_page.html', context)

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
        'delete_url' : 'delete_user',
    }

    return render(request, 'common/particular.html', context)
