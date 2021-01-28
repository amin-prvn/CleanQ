from rest_framework import serializers

from .models import Reservation, Clinic, Patient
from .validators import phone_number

# import pdb; pdb.set_trace()
import  datetime
START_TIME = datetime.time(hour=8)

class ClinicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = ('email', 'password', 'name', 'address', 'phone', 'description')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        clinic = Clinic(**validated_data)
        clinic.set_password()
        clinic.save()
        return clinic

    def update(self, instance, validated_data):
        for key, item in validated_data.items():
            setattr(instance, key, item)
            if key == 'password': 
                instance.set_password()
        instance.save()
        return instance


class PatientSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(validators=[phone_number])

    class Meta:
        model = Patient
        fields = ('email', 'password', 'name', 'phone')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        patient = Patient(**validated_data)
        patient.set_password()
        patient.save()
        return patient

    def update(self, instance, validated_data):
        for key, item in validated_data.items():
            setattr(instance, key, item)
            if key == 'password': 
                instance.set_password()
        instance.save()
        return instance


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('clinic', 'description')

    def create(self, validated_data):

        
