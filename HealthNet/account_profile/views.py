from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from registration.models import Patient, Doctor 
from .forms import UpdatePatientForm, UpdateDoctorForm
from django.views.generic import UpdateView

from activity_log.models import Log
from django.utils import timezone

from django.shortcuts import render, redirect

# Create your views here.

@login_required
def index(request):
    try: 
        patient = Patient.objects.filter(user=request.user).first()
    except:
        patient = None
    try:
        doctor = Doctor.objects.get(user=request.user).first()
    except:
        doctor = None

    if patient:
        context = {
            'patient': patient
        }
    else: 
        context = {
            'doctor': doctor
        }
    return render(request, 'account_profile/index.html', context)

@login_required
def edit_p(request): 
    instance = Patient.objects.filter(user=request.user).first()
    form = UpdatePatientForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        Log.create_log(Log, 
                       request.user.username, 
                       " has updated their profile.", 
                       timezone.now())

        return redirect('/profile')

    return render(request, 
                  'edit.html',
                  {'form': form})     


@login_required
def edit_d(request): 
    instance = Doctor.objects.filter(user=request.user).first()
    form = UpdateDoctorForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        Log.create_log(Log, request.user.username, " has updated their profile.", timezone.now())
        return redirect('/profile')
    return render(request, 'edit.html', {'form': form})  
