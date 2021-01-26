from django.db import models
from django.contrib.auth.hashers import (
    check_password, make_password,
)
from .manager import ClinicManager, PatientManager


class BaseUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

class Clinic(BaseUser):
    address = models.TextField()
    description = models.TextField()
    active = models.BooleanField(default=False)
    objects = ClinicManager()

    def __str__(self):
        return self.email

    def set_password(self):
        self.password = make_password(self.password)



class Patient(BaseUser):
    objects = PatientManager()

    def __str__(self):
        return self.email

    def set_password(self):
        self.password = make_password(self.password)



class Reservation(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f" {self.clinic.name} | {self.patient.name} | {self.time} "
    



