from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def landing_page(request):
    return render(request, 'users/users_landing.html', {})


def all_users(request):
    users = User.objects.all()

    context = { 'users' : users }

    return render(request, 'users/all_users.html', context)


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


def search_user(request):
    return render(request, 'users/users_landing.html', {})


def particular_user(request, user_id):
    desired_user = User.objects.get(pk=user_id)

    if desired_user == None:
        context = {
            'message': 'the desired user does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'user': desired_user
    }

    return render(request, 'users/particular_user_page.html', context)
