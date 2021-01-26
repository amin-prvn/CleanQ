from django.urls import path, include
from .views import  ClinicView, PatientView

urlpatterns = [
    path('clinic', ClinicView.as_view()),
    path('patient', PatientView.as_view()),
]