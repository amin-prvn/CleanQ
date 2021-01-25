from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=128, primary_key=True, db_index=True)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f" {self.clinic.name} | {self.patient.name} | {self.time} "
    



