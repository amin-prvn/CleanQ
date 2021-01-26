from rest_framework import serializers

from .models import Reservation, Clinic, Patient
from .validators import phone_number


class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = ('email', 'password', 'name', 'address', 'phone', 'description')

    # def create(self, validated_data):
    #     clinic = Clinic(**validated_data)
    #     clinic.set_password()
    #     clinic.save()
    #     return clinic


class PatientSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(validators=[phone_number])

    class Meta:
        model = Patient
        fields = ('email', 'password', 'name', 'phone')


