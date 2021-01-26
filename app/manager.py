from django.db import models


class ClinicManager(models.Manager):

    def create_clinic(self,**extra_fields):
        clinic = self.model(**extra_fields)
        clinic.set_password()
        clinic.save(using=self._db)
        return clinic


class PatientManager(models.Manager):

    def create_patient(self,**extra_fields):
        patient = self.model(**extra_fields)
        patient.set_password()
        patient.save(using=self._db)
        return patient
