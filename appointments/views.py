from django.shortcuts import render
from .models import Appointment, Annotation_Appointment
from .forms import AppointmentForm, AnnotationForm
from pets.models import Pet

# Create your views here.
def landing_page(request):
    appointments = Appointment.objects.all()

    context = {
        'page_name': 'Appointments',
	    'object_name': 'appointment',
	    'all_url': 'all_appointments',
	    'register_url': 'register_appointment',
	    'desired_image_url': 'appointments/images/vet_examining.png',
	    'image_alt_name':  'Vet examining cat',
        'objects': appointments,
        'base_url': 'particular_appointment',
        'can_create': True,
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


def register_appointment(request, pet_id=None):
    form = AppointmentForm(pet=pet_id, is_creating=True)

    if request.method == 'POST':
        if pet_id:
            form = AppointmentForm(request.POST, pet=pet_id)
        else:
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
        'editable': True,
        'is_appointment': True,
    }

    return render(request, 'common/particular.html', context)




# For the annotations
def all_annotations(request, appointment_id):
    annotations = Annotation_Appointment.objects.filter(appointment_id=appointment_id)

    context = {
        'page_name' : 'Annotations',
	    'object_name' : 'annotation',
	    'all_url' : 'all_annotations',
	    'register_url' : 'register_annotation',
	    'desired_image_url' : '',
	    'image_alt_name' :  '',
        'objects' : annotations,
        'base_url' : 'particular_annotation',
        'is_annotation': True,
        'appointment_id': appointment_id,
    }
    
    return render(request, 'common/landing.html', context)


def register_annotation(request, appointment_id):
    form = AnnotationForm(appointment_id=appointment_id)

    if request.method == 'POST':
        form = AnnotationForm(request.POST, appointment_id=appointment_id)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Registro De Nota Exitoso',
                'return_page_name' : 'Annotations',
                'desired_url' : 'annotations_appointment',
                'is_annotation': True,
                'appoinment_id': appointment_id,
                'is_annotation': True,
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible registrar el nota',
                'return_page_name' : 'Annotations',
                'desired_url' : 'annotations_appointment',
                'appoinment_id': appointment_id,
                'is_annotation': True,
            }
            return render(request, 'common/result_page.html', context)

    context = { 
        'form': form,
        'page_name' : 'Register Annotation'
    }
    return render(request, 'common/register.html', context)


def edit_annotation(request, appointment_id, annotation_id):
    try:
        desired_annotation = Annotation_Appointment.objects.get(pk=annotation_id)
    except Annotation_Appointment.DoesNotExist:
        context = {
            'message': 'the desired annotation does not exist',
            'return_page_name': 'home page',
            'desired_url': 'main_page',
            'appoinment_id': appointment_id,
            'is_annotation': True,
        }
        return render(request, 'common/result_page.html', context)

    if request.method == 'POST':
        form = AnnotationForm(request.POST, instance=desired_annotation)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Actualizacion De Nota Exitoso',
                'return_page_name' : 'Annotations',
                'desired_url' : 'annotations_appointment',
                'appoinment_id': appointment_id,
                'is_annotation': True,
            }
            return render(request, 'common/result_page.html', context)
        else:
            context = {
                'message': 'No fue posible actualizar el nota',
                'return_page_name' : 'Annotations',
                'desired_url' : 'annotations_appointment',
                'appoinment_id': appointment_id,
                'is_annotation': True,
            }
            return render(request, 'common/result_page.html', context)
    
    form = AnnotationForm(appointment_id=appointment_id, instance=desired_annotation)

    context = { 
        'page_name' : 'Edit Annotation',
        'object': desired_annotation,
        'form': form,
    }
    return render(request, 'common/edit.html', context)


def delete_annotation(request, appointment_id, annotation_id):
    try:
        desired_annotation = Annotation_Appointment.objects.get(pk=annotation_id)
    except Annotation_Appointment.DoesNotExist:
        context = {
            'message': 'the desired annotation does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page',
            'appoinment_id': appointment_id,
            'is_annotation': True,
        }
        return render(request, 'common/result_page.html', context)
    
    desired_annotation.delete()
    context = {
        'message': 'El nota fue eliminado exitosamente',
        'return_page_name' : 'Annotations',
        'desired_url' : 'annotations_appointment',
        'appoinment_id': appointment_id,
        'is_annotation': True,
    }
    return render(request, 'common/result_page.html', context)


def particular_annotation(request, appointment_id, annotation_id):
    try:
        desired_annotation = Annotation_Appointment.objects.get(pk=annotation_id)
    except Annotation_Appointment.DoesNotExist:
        context = {
            'message': 'the desired annotation does not exits',
            'return_page_name': 'home page',
            'desired_url': 'main_page',
            'appoinment_id': appointment_id,
            'is_annotation': True,
        }
        return render(request, 'common/result_page.html', context)

    context = {
        'page_name' : 'Annotation',
        'object': desired_annotation,
        'edit_url' : 'edit_annotation',
        'delete_url' : 'delete_annotation',
        'editable': True,
    }

    return render(request, 'common/particular.html', context)

