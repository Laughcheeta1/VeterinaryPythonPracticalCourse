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
            print("It was succesfull")
            # TODO: make the response be a page
            return HttpResponse("Submission was successful")
        else:
            print("It was not succesfull")
            return HttpResponse("unsecces")

    context = { 'form': form }
    return render(request, 'users/register_user.html', context)

def search_user(request):
    return render(request, 'users/users_landing.html', {})

def particular_user(request):
    return render(request, 'users/users_landing.html', {})
