from django.shortcuts import render
from .models import Surgery
from .forms import SurgeryForm

# Create your views here.
def landing_page(request):
    context = {
        'page_name' : 'Surgeries',
	    'object_name' : 'surgery',
	    'all_url' : 'all_surgeries',
	    'register_url' : 'register_surgery',
	    'desired_image_url' : 'surgeries/images/surgeon.png',
	    'image_alt_name' :  'Surgeon',
    }
    return render(request, 'common/landing.html', context)


def all_surgeries(request):
    surgeries = Surgery.objects.all()

    context = { 
        'objects' : surgeries,
        'page_name' : 'All Surgeries',
        'base_url' : 'particular_surgery'
    }

    return render(request, 'common/all.html', context)


def register_surgery(request):
    form = SurgeryForm()

    if request.method == 'POST':
        form = SurgeryForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Cirugia Exitoso',
                'return_page_name' : 'Surgeries',
                'desired_url' : 'surgeries_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar la cirugia',
                'return_page_name' : 'Surgeries',
                'desired_url' : 'surgeries_landing_page'
            }
            return render(request, 'common/result_page.html', context)

    context = { 
        'form': form,
        'page_name' : 'Register Surgery'
    }
    return render(request, 'common/register.html', context)


def edit_surgery(request, surgery_id):
    try:
        desired_surgery = Surgery.objects.get(pk=surgery_id)
    except Surgery.DoesNotExist:
        context = {
            'message': 'the desired surgery does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = SurgeryForm(request.POST, instance=desired_surgery)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Actualizacion De Cirugia Exitoso',
                'return_page_name' : 'Surgeries',
                'desired_url' : 'surgeries_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible actualizar la cirugia',
                'return_page_name' : 'Surgeries',
                'desired_url' : 'surgeries_landing_page'
            }
            return render(request, 'common/result_page.html', context)
    
    form = SurgeryForm(instance=desired_surgery)

    context = { 
        'page_name' : 'Edit Surgery',
        'object': desired_surgery,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def delete_surgery(request, surgery_id):
    try:
        desired_surgery = Surgery.objects.get(pk=surgery_id)
    except Surgery.DoesNotExist:
        context = {
            'message': 'the desired surgery does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)
    
    desired_surgery.delete()
    context = {
        'message': 'La cirugia fue eliminado exitosamente',
        'return_page_name' : 'Surgeries',
        'desired_url' : 'surgeries_landing_page'
    }
    return render(request, 'common/result_page.html', context)

def particular_surgery(request, surgery_id):
    try:
        desired_surgery = Surgery.objects.get(pk=surgery_id)
    except Surgery.DoesNotExist:
        context = {
            'message': 'the desired surgery does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'Surgery',
        'object': desired_surgery,
        'edit_url' : 'edit_surgery',
        'delete_url' : 'delete_surgery',
    }

    return render(request, 'common/particular.html', context)
