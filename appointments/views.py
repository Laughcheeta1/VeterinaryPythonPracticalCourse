from django.shortcuts import render
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.
def landing_page(request):
    context = {
        'page_name' : 'Appointments',
	    'object_name' : 'appointment',
	    'all_url' : 'all_appointments',
	    'register_url' : 'register_appointment',
	    'desired_image_url' : 'appointments/images/vet_examining.png',
	    'image_alt_name' :  'Vet examining cat',
    }
    return render(request, 'common/landing.html', context)


def all_appointments(request):
    appointments = Appointment.objects.all()

    context = { 
        'objects' : appointments,
        'page_name' : 'All Appointments',
        'base_url' : 'particular_appointment'
    }

    return render(request, 'common/all.html', context)


def register_appointment(request):
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Cita Exitosa',
                'return_page_name' : 'Appointments',
                'desired_url' : 'appointments_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar la cita',
                'return_page_name' : 'Appointments',
                'desired_url' : 'appointments_landing_page'
            }
            return render(request, 'common/result_page.html', context)

    context = { 
        'form': form,
        'page_name' : 'Register Appointment'
    }
    return render(request, 'common/register.html', context)


def edit_appointment(request, appointment_id):
    try:
        desired_appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        context = {
            'message': 'the desired appointment does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=desired_appointment)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Actualizacion De Cita Exitosa',
                'return_page_name' : 'Appointments',
                'desired_url' : 'appointments_landing_page'
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible actualizar la cita',
                'return_page_name' : 'Appointments',
                'desired_url' : 'appointments_landing_page'
            }
            return render(request, 'common/result_page.html', context)
    
    form = AppointmentForm(instance=desired_appointment)

    context = { 
        'page_name' : 'Edit Appointment',
        'object': desired_appointment,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def delete_appointment(request, appointment_id):
    try:
        desired_appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        context = {
            'message': 'the desired appointment does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)
    
    desired_appointment.delete()
    context = {
        'message': 'La cita fue eliminada exitosamente',
        'return_page_name' : 'Appointments',
        'desired_url' : 'appointments_landing_page'
    }
    return render(request, 'common/result_page.html', context)

def particular_appointment(request, appointment_id):
    try:
        desired_appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        context = {
            'message': 'the desired appointment does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page'
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'Appointment',
        'object': desired_appointment,
        'edit_url' : 'edit_appointment',
        'delete_url' : 'delete_appointment',
    }

    return render(request, 'common/particular.html', context)
