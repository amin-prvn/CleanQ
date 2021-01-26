from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClinicSerializer, PatientSerializer
from .models import Clinic, Patient
from .authentication import Auth


class ClinicView(APIView):

    def get(self, request):
        queryset = Clinic.objects.filter(active=True)
        serializer = ClinicSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClinicSerializer(data = request.data)
        if serializer.is_valid():
            clinic = Clinic.objects.create_clinic(**serializer.validated_data)
            token = Auth.generate_token(clinic.id, 'clinic')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientView(APIView):

    def post(self, request):
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            patient = Patient.objects.create_patient(**serializer.validated_data)
            token = Auth.generate_token(patient.id, 'patient')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @Auth.auth_required('patient')
    def get(self, request, *args, **kwargs):
        print(kwargs)
        return Response("ok")



            
        
