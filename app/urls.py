from django.urls import path, include
from .views import  *

urlpatterns = [
    path('clinic', ClinicView.as_view()),
]