from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *
from .authentication import Auth


class ClinicView(APIView):

    def get(self, request):
        queryset = Clinic.objects.filter(active=True)
        serializer = ClinicSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClinicSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            token = Auth.generate_token(serializer.id, 'clinic')
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




            
        
