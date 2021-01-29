from django.contrib import admin

from .models import *


class ReservationInline(admin.StackedInline):
    model = Reservation
    extra = 0

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    inlines = [ReservationInline,]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = [ReservationInline,]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass