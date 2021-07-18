from rest_framework import serializers
from  datetime import datetime, timedelta

from .models import Reservation, Clinic, Patient
from .validators import phone_number

# Static start hour of day for all reservations
START_TIME = 10
# Static end hour of day for all reservations
END_TIME = 20
# Static delta time for all reservations
DELTA_TIME = 30


class ReservationSerializer(serializers.ModelSerializer):
    '''
        Reservation serializer class
    '''

    class Meta:
        model = Reservation
        fields = ('patient', 'clinic', 'time', 'description')
        extra_kwargs = {
            'patient': {'read_only': True},
            'time': {'read_only': True},
        }

    def create(self, validated_data):
        clinic_id = validated_data['clinic'].id
        patient = Patient.objects.get(pk=validated_data['patient'])
        now = datetime.now()
        try:
            last_reservation = Reservation.objects.filter(clinic=clinic_id).latest('time')

            # Today
            if last_reservation.time.date() == now.date():

                if last_reservation.time.hour >= END_TIME:
                    time = tomorrow(last_reservation.time)

                elif last_reservation.time.hour >= now.hour:
                    time = before_or_after_delta(last_reservation.time)
                
                elif last_reservation.time.hour < now.hour:
                    time = before_or_after_delta(now)

            # Before Today
            elif last_reservation.time.date() < now.date():

                if now.hour >= END_TIME:
                    time = tomorrow(now)

                else:
                    time = before_or_after_delta(now)

            # After Today
            elif last_reservation.time.date() > now.date():

                if last_reservation.time.hour >= END_TIME:
                    time = tomorrow(last_reservation.time)

                else:
                    time = before_or_after_delta(last_reservation.time)
    
            reservation = Reservation.objects.create(
                patient=patient, 
                clinic=validated_data['clinic'],
                description=validated_data.get('description'), 
                time=time
                )

        except Reservation.DoesNotExist:

            if now.hour >= END_TIME:
                    time = tomorrow(now)
            else:
                time = before_or_after_delta(now)

            reservation = Reservation.objects.create(
                patient=patient, 
                clinic=validated_data['clinic'],
                description=validated_data.get('description'), 
                time=time
                )
        return reservation


class ClinicSerializer(serializers.ModelSerializer):
    '''
        Clinic Serializer class
    '''

    class Meta:
        model = Clinic
        fields = ('id', 'email', 'password', 'name', 'address', 'phone', 'description')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    # Create clinic and hashed password
    def create(self, validated_data):
        clinic = Clinic(**validated_data)
        clinic.set_password()
        clinic.save()
        return clinic

    # Update clinic and hashed password
    def update(self, instance, validated_data):
        for key, item in validated_data.items():
            setattr(instance, key, item)
            if key == 'password': 
                instance.set_password()
        instance.save()
        return instance


class PatientSerializer(serializers.ModelSerializer):
    '''
        Patient Serializer class
    '''

    phone = serializers.CharField(validators=[phone_number])

    class Meta:
        model = Patient
        fields = ('email', 'password', 'name', 'phone')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    # Create patient and hashed password
    def create(self, validated_data):
        patient = Patient(**validated_data)
        patient.set_password()
        patient.save()
        return patient
    
    # Update patient and hashed password
    def update(self, instance, validated_data):
        for key, item in validated_data.items():
            setattr(instance, key, item)
            if key == 'password': 
                instance.set_password()
        instance.save()
        return instance


# Check time is before or after static delta time?
def before_or_after_delta(time):
    if time.minute >= DELTA_TIME :
        print('after')
        time += timedelta(hours=1)
        return time.replace(minute=0, second=0, microsecond=0)
    else:
        print('before')
        return time.replace(minute=DELTA_TIME, second=0, microsecond=0)

# Return tomorrow time if latest time is bigger or equal than end time of the day
def tomorrow(time):
    print('tomorrow')
    time += timedelta(days=1)
    return time.replace(hour=START_TIME, minute=0, second=0, microsecond=0)
    


        
