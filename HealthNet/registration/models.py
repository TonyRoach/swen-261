from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateTimeField('date of birth', blank=True)
    height = models.FloatField(blank=True)
    weight = models.FloatField(blank=True)
    insurer = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return User.get_full_name(self.user)

    def htmlName(self):
        return User.get_full_name(self.user)

    def get_absolute_url(self):
        return '/profile/'

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    specialty = models.CharField(max_length=20)

    def __str__(self):
        return User.get_full_name(self.user)

    def htmlName(self):
        return User.get_full_name(self.user)

    def get_absolute_url(self):
        return '/profile/'