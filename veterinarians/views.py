from django.shortcuts import render
from .models import Veterinarian
from .forms import VeterinarianForm
import csv
from django.http import HttpResponse

# Create your views here.
def landing_page(request):
    veterinarians = Veterinarian.objects.all()

    context = {
        'page_name' : 'Veterinarians',
	    'object_name' : 'veterinarian',
	    'all_url' : 'all_veterinarians',
	    'register_url' : 'register_veterinarian',
	    'desired_image_url' : 'veterinarians/images/veterinarians.png',
	    'image_alt_name' :  'Group of veterinaries posing',
        'objects' : veterinarians,
        'base_url' : 'particular_veterinarian',
    }
    
    return render(request, 'common/landing.html', context)


def all_veterinarians(request):
    veterinarians = Veterinarian.objects.all()

    context = { 
        'objects' : veterinarians,
        'page_name' : 'All Veterinarians',
        'base_url' : 'particular_veterinarian'
    }

    return render(request, 'common/all.html', context)


def register_veterinarian(request):
    form = VeterinarianForm()

    if request.method == 'POST':
        form = VeterinarianForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Veterinario Exitoso',
                'return_page_name' : 'Veterinarians',
                'desired_url' : 'veterinarians_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar el veterinario',
                'return_page_name' : 'Veterinarians',
                'desired_url' : 'veterinarians_landing_page'
            }
            return render(request, 'common/result_page.html', context)

    context = { 
        'form': form,
        'page_name' : 'Register Veterinarian'
    }
    return render(request, 'common/register.html', context)


def edit_veterinarian(request, veterinarian_id):
    try:
        desired_veterinarian = Veterinarian.objects.get(pk=veterinarian_id)
    except Veterinarian.DoesNotExist:
        context = {
            'message': 'the desired veterinarian does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = VeterinarianForm(request.POST, instance=desired_veterinarian)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Actualizacion De Veterinario Exitoso',
                'return_page_name' : 'Veterinarians',
                'desired_url' : 'veterinarians_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible actualizar el veterinario',
                'return_page_name' : 'Veterinarians',
                'desired_url' : 'veterinarians_landing_page'
            }
            return render(request, 'common/result_page.html', context)
    
    form = VeterinarianForm(instance=desired_veterinarian)

    context = { 
        'page_name' : 'Edit Veterinarian',
        'object': desired_veterinarian,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def delete_veterinarian(request, veterinarian_id):
    try:
        desired_veterinarian = Veterinarian.objects.get(pk=veterinarian_id)
    except Veterinarian.DoesNotExist:
        context = {
            'message': 'the desired veterinarian does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)
    
    desired_veterinarian.delete()
    context = {
        'message': 'El veterinario fue eliminado exitosamente',
        'return_page_name' : 'Veterinarians',
        'desired_url' : 'veterinarians_landing_page'
    }
    return render(request, 'common/result_page.html', context)


def particular_veterinarian(request, veterinarian_id):
    try:
        desired_veterinarian = Veterinarian.objects.get(pk=veterinarian_id)
    except Veterinarian.DoesNotExist:
        context = {
            'message': 'the desired veterinarian does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'Veterinarian',
        'object': desired_veterinarian,
        'edit_url' : 'edit_veterinarian',
        'delete_url' : 'delete_veterinarian',
    }

    return render(request, 'common/particular.html', context)


def download_csv():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="veterinarians.csv"'

    writer = csv.writer(response)
    fields = [field.name for field in Veterinarian._meta.fields]
    writer.writerow(fields)

    for vet in Veterinarian.objects.all():
        writer.writerow([getattr(vet, field) for field in fields])

    return response
