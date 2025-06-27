from django.shortcuts import render
from .models import Pet
from .forms import PetForm

# Create your views here.
def landing_page(request):
    context = {
        'page_name' : 'Pets',
	    'object_name' : 'pet',
	    'all_url' : 'all_pets',
	    'register_url' : 'register_pet',
	    'desired_image_url' : '',
	    'image_alt_name' :  '',
    }
    return render(request, 'common/landing.html', context)


def all_users(request):
    pets = Pet.objects.all()

    context = { 
        'objects' : pets,
        'page_name' : 'All Pets',
        'base_url' : 'particular_pet'
    }

    return render(request, 'common/all.html', context)


def register_user(request):
    form = PetForm()

    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Mascota Exitoso',
                'return_page_name' : 'Mascotas',
                'desired_url' : 'pets_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar la mascota',
                'return_page_name' : 'Mascotas',
                'desired_url' : 'pets_landing_page'
            }
            return render(request, 'common/result_page.html', context)

    context = { 
        'form': form,
        'page_name' : 'Register Pet'
    }
    return render(request, 'common/register.html', context)


def edit_user(request, pet_id):
    try:
        desired_pet = Pet.objects.get(pk=pet_id)
    except Pet.DoesNotExist:
        context = {
            'message': 'the desired pet does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Mascota Exitoso',
                'return_page_name' : 'Mascotas',
                'desired_url' : 'pets_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar la mascota',
                'return_page_name' : 'Pets',
                'desired_url' : 'pets_landing_page'
            }
            return render(request, 'common/result_page.html', context)
    
    form = PetForm(instance=desired_pet)

    context = { 
        'page_name' : 'Edit User',
        'object': desired_pet,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def delete_user(request, pet_id):
    try:
        desired_pet = Pet.objects.get(pk=pet_id)
    except Pet.DoesNotExist:
        context = {
            'message': 'the desired pet does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)
    
    desired_pet.delete()
    context = {
        'message': 'La mascota fue eliminada exitosamente',
        'return_page_name' : 'Mascotas',
        'desired_url' : 'pets_landing_page'
    }
    return render(request, 'common/result_page.html', context)


def particular_user(request, pet_id):
    try:
        desired_pet = Pet.objects.get(pk=pet_id)
    except Pet.DoesNotExist:
        context = {
            'message': 'the desired pet does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'Mascota',
        'object': desired_pet,
        'edit_url' : 'edit_pet',
        'delete_url' : 'delete_pet',
    }

    return render(request, 'common/particular.html', context)
