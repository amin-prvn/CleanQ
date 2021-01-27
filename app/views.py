from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters


from .serializers import ClinicSerializer, PatientSerializer
from .models import Clinic, Patient
from .authentication import Auth


class GetClinic(ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class ClinicView(APIView):

    def post(self, request):
        serializer = ClinicSerializer(data = request.data)
        if serializer.is_valid():
            # clinic = Clinic.objects.create_clinic(**serializer.validated_data)
            serializer.save()
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

    def post(self, request):
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            patient = Patient.objects.create_patient(**serializer.validated_data)
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
        
