from django import forms
from django.forms import ModelForm
from registration.models import Doctor, Patient

class UpdatePatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['dateOfBirth', 'height', 'weight', 'insurer', 'address']

class UpdateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialty']
