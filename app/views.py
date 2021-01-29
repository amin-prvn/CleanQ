from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from .serializers import GetClinicSerializer, ClinicSerializer, PatientSerializer, ReservationSerializer
from .models import Clinic, Patient, Reservation
from .authentication import Auth


class GetClinic(ListAPIView):
    queryset = Clinic.objects.filter(active=True)
    serializer_class = GetClinicSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ClinicView(APIView):

    @Auth.auth_required('clinic')
    def get(self, request, *args, **kwargs):
        queryset = Clinic.objects.get(pk=kwargs['id'])
        serializer = ClinicSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = ClinicSerializer(data = request.data)
        if serializer.is_valid():
            clinic = serializer.save()
            token = Auth.generate_token(clinic.id, 'clinic')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @Auth.auth_required('clinic')
    def put(self, request, *args, **kwargs):
        clinic = Clinic.objects.get(pk=kwargs['id'])
        serializer = ClinicSerializer(clinic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @Auth.auth_required('clinic')
    def delete(self, request, *args, **kwargs):
        clinic = Clinic.objects.get(pk=kwargs['id'])
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
        
class PatientView(APIView):

    @Auth.auth_required('patient')
    def get(self, request, *args, **kwargs):
        queryset = Patient.objects.get(pk=kwargs['id'])
        serializer = PatientSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            patient = serializer.save()
            token = Auth.generate_token(patient.id, 'patient')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @Auth.auth_required('patient')
    def put(self, request, *args, **kwargs):
        patient = Patient.objects.get(pk=kwargs['id'])
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @Auth.auth_required('patient')
    def delete(self, request, *args, **kwargs):
        patient = Clinic.objects.get(pk=kwargs['id'])
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
class CreateReservation(APIView):

    @Auth.auth_required('patient')
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            reservation = serializer.save(patient = kwargs['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ClinicReservation(APIView):

#     @Auth.auth_required('clinic')
#     def get(self, request, *args, **kwargs):
#         queryset = Reservation.objects.filter(clinic=kwargs['id'])
#         serializer = ReservationSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class PatientReservation(APIView):

#     @Auth.auth_required('patient')
#     def get(self, request, *args, **kwargs):
#         queryset = Reservation.objects.filter(clinic=kwargs['id'])
#         serializer = ReservationSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
