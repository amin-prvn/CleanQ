from django.contrib import admin
import os 
from django.core.files.base import ContentFile, File


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

@admin.register(BackUp)
class BackUpAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
            os.system('sudo -u postgres pg_dump -p 5433 -U postgres -d cleanq >> cleanq.db')
            file  = open('cleanq.db', 'rb')
            obj.file = File(file)
            obj.save()
            
            
@admin.register(Restore)
class RestoreAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        os.system(f'sudo -u postgres psql -p 5433 -U postgres -d cleanq -f {obj.path}')