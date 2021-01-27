from rest_framework import serializers

from .models import Reservation, Clinic, Patient
from .validators import phone_number


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
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.password = validated_data.get('password')
            instance.set_password()
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.description = validated_data.get('description', instance.description)
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
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.password = validated_data.get('password')
            instance.set_password()
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


