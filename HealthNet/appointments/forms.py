from django import forms
from .models import Appointment
from activity_log.models import Log
from registration.models import Patient, Doctor

class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label=None)
        doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label=None)
        fields = ['time', 'location', 'patient', 'doctor']
