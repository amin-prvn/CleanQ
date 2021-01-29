from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from datetime import datetime

from .serializers import ClinicSerializer, PatientSerializer, ReservationSerializer
from .models import Clinic, Patient, Reservation
from .authentication import Auth


class GetClinic(ListAPIView):
    '''
        Get all active clinics
    '''
    queryset = Clinic.objects.filter(active=True)
    serializer_class = ClinicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ClinicView(APIView):
    '''
        Clinic view class
    '''

    # Get clinic's reservations with token
    @Auth.auth_required('clinic')
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        params = request.query_params
        if params.get('ordering') == 'past':
            queryset = Reservation.objects.filter(clinic=kwargs['id'], time__lt=now)
        elif params.get('ordering') == 'upcoming':
            queryset = Reservation.objects.filter(clinic=kwargs['id'], time__gte=now)
        else :
            queryset = Reservation.objects.filter(clinic=kwargs['id'])
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create clinic and get token response
    def post(self, request):
        serializer = ClinicSerializer(data = request.data)
        if serializer.is_valid():
            clinic = serializer.save()
            token = Auth.generate_token(clinic.id, 'clinic')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Edit clinic with token authentication
    @Auth.auth_required('clinic')
    def put(self, request, *args, **kwargs):
        clinic = Clinic.objects.get(pk=kwargs['id'])
        serializer = ClinicSerializer(clinic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete clinic with token authentication
    @Auth.auth_required('clinic')
    def delete(self, request, *args, **kwargs):
        clinic = Clinic.objects.get(pk=kwargs['id'])
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
        
class PatientView(APIView):
    '''
        Patient view class
    '''

    # Get patient's reservations with token
    @Auth.auth_required('patient')
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        params = request.query_params
        if params.get('ordering') == 'past':
            queryset = Reservation.objects.filter(patient=kwargs['id'], time__lt=now)
        elif params.get('ordering') == 'upcoming':
            queryset = Reservation.objects.filter(patient=kwargs['id'], time__gte=now)
        else :
            queryset = Reservation.objects.filter(patient=kwargs['id'])
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create patient and get token response
    def post(self, request):
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            patient = serializer.save()
            token = Auth.generate_token(patient.id, 'patient')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Edit patient with token authentication
    @Auth.auth_required('patient')
    def put(self, request, *args, **kwargs):
        patient = Patient.objects.get(pk=kwargs['id'])
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete patient with token authentication
    @Auth.auth_required('patient')
    def delete(self, request, *args, **kwargs):
        patient = Clinic.objects.get(pk=kwargs['id'])
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
class ReservationView(APIView):
    '''
        Reservation view class
    '''

    # Create reservation for patient with patient's token 
    @Auth.auth_required('patient')
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            reservation = serializer.save(patient = kwargs['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

