import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Medications
from .forms import MedicationsForm

# Create your views here.
def landing_page(request):
    medications = Medications.objects.all()

    context = {
        'page_name' : 'Medications',
	    'object_name' : 'medication',
	    'all_url' : 'all_medications',
	    'register_url' : 'register_medication',
	    'desired_image_url' : 'medications/images/medicines.png',
	    'image_alt_name' :  'Veterinarian grabbing medicines',
        'objects' : medications,
        'base_url' : 'particular_medication',
    }
    
    return render(request, 'common/landing.html', context)


def all_medications(request):
    medications = Medications.objects.all()

    context = { 
        'objects' : medications,
        'page_name' : 'All Medications',
        'base_url' : 'particular_medication'
    }

    return render(request, 'common/all.html', context)


def register_medication(request):
    form = MedicationsForm()

    if request.method == 'POST':
        form = MedicationsForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Medicamento Exitoso',
                'return_page_name' : 'Medications',
                'desired_url' : 'medications_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar el medicamento',
                'return_page_name' : 'Medications',
                'desired_url' : 'medications_landing_page'
            }
            return render(request, 'common/result_page.html', context)

    context = { 
        'form': form,
        'page_name' : 'Register Medication'
    }
    return render(request, 'common/register.html', context)


def edit_medication(request, medication_id):
    try:
        desired_medication = Medications.objects.get(pk=medication_id)
    except Medications.DoesNotExist:
        context = {
            'message': 'the desired medication does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = MedicationsForm(request.POST, instance=desired_medication)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Actualizacion De Medicamento Exitoso',
                'return_page_name' : 'Medications',
                'desired_url' : 'medications_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible actualizar el medicamento',
                'return_page_name' : 'Medications',
                'desired_url' : 'medications_landing_page'
            }
            return render(request, 'common/result_page.html', context)
    
    form = MedicationsForm(instance=desired_medication)

    context = { 
        'page_name' : 'Edit Medication',
        'object': desired_medication,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def delete_medication(request, medication_id):
    try:
        desired_medication = Medications.objects.get(pk=medication_id)
    except Medications.DoesNotExist:
        context = {
            'message': 'the desired medication does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)
    
    desired_medication.delete()
    context = {
        'message': 'El medicamento fue eliminado exitosamente',
        'return_page_name' : 'Medications',
        'desired_url' : 'medications_landing_page'
    }
    return render(request, 'common/result_page.html', context)


def particular_medication(request, medication_id):
    try:
        desired_medication = Medications.objects.get(pk=medication_id)
    except Medications.DoesNotExist:
        context = {
            'message': 'the desired medication does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'Medication',
        'object': desired_medication,
        'edit_url' : 'edit_medication',
        'delete_url' : 'delete_medication',
    }

    return render(request, 'common/particular.html', context)


def download_csv():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="medications.csv"'

    writer = csv.writer(response)
    fields = [field.name for field in Medications._meta.fields]
    writer.writerow(fields)

    for medication in Medications.objects.all():
        writer.writerow([getattr(medication, field) for field in fields])

    return response