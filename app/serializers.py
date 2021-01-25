from rest_framework import serializers

from .models import Reservation, Clinic, Patient
from .validators import phone_number


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = ('name', 'address', 'phone', 'description')


class PatientSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(validators=[phone_number])

    class Meta:
        model = Patient
        fields = ('name', 'phone')


