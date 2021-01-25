from django.contrib import admin
from .models import *


@admin.register(Clinic)
class youtuber_admin(admin.ModelAdmin):
    pass