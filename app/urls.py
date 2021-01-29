from django.urls import path, include
from .views import ClinicView, PatientView, GetClinic, ReservationView

urlpatterns = [
    path('clinic', ClinicView.as_view()),
    path('patient', PatientView.as_view()),
    path('get-clinics', GetClinic.as_view()),
    path('reserve', ReservationView.as_view()),
]