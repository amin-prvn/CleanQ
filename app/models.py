from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Clinic(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)    
    name = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = None
    user_permissions = None

    REQUIRED_FIELDS = [email]

    def __str__(self):
        return self.email


class Patient(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    phone = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f" {self.clinic.name} | {self.patient.name} | {self.time} "
    



