from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User

from .models import Appointment
from .forms import UpdateAppointmentForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from activity_log.models import Log
from django.utils import timezone
from registration.models import Patient, Doctor

@login_required
def index(request):
    appointment_list = Appointment.objects.order_by('-time')[:5]
    try: 
        patient = Patient.objects.filter(user=request.user).first()
        appointment_list = Appointment.objects.get(patient=patient).order_by('-time')[:5]
    except:
        patient = None
    try:
        doctor = Doctor.objects.get(user=request.user).first()
        appointment_list = Appointment.objects.get(doctor=doctor).order_by('-time')[:5]
    except:
        doctor = None
    context = {
        'appointment_list': appointment_list
    }
    return render(request, 'index.html', context)

@login_required
def detail(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        raise Http404("Appointment does not exist")
    return render(request, 'detail.html', {'appointment': appointment})

class DeleteAppointment(DeleteView):
    model = Appointment
    template_name = 'delete.html'
    success_url = '/appointments/'

class CreateAppointment(CreateView):
    model = Appointment
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label=None)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label=None)
    template_name = 'create.html'
    success_url = '/appointments/'
    fields = ['time', 'location', 'patient', 'doctor']
@login_required
def edit(request, appointment_id): 
    instance = get_object_or_404(Appointment, id=appointment_id)
    form = UpdateAppointmentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        Log.create_log(Log,
                       request.user.username, 
                       " has updated one of their appointments.", 
                       timezone.now())
        return redirect('/appointments')

    return render(request, 'edit.html', {'form': form})     

