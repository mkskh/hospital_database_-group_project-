from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import PatientSerializer
from .models import Patient
from .filters import PatientFilter

from datetime import datetime
import requests

response = requests.get('https://dummyjson.com/users')

users_data = response.json().get('users', [])

# def index(request):
#     return render(request, 'patients/index.html')

class PatientView(ListCreateAPIView):
    
    serializer_class = PatientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PatientFilter
    
    def get_queryset(self):
        
        for user_data in users_data:
            birthdate = datetime.strptime(user_data['birthDate'], "%Y-%m-%d").date()
            Patient.objects.update_or_create(
                email=user_data['email'],
                defaults={
                    'firstname':user_data['firstName'],
                    'lastname':user_data['lastName'],
                    'maidenname':user_data['maidenName'],
                    'age':user_data['age'],
                    'gender':user_data['gender'],
                    'phone':user_data['phone'],
                    'bloodgroup': user_data['bloodGroup'],
                    'birthdate': birthdate,
                    'height' : user_data['height'],
                    'weight': user_data['weight'],
                    'eyecolor': user_data['eyeColor'],
                }
            )
        
        return Patient.objects.all()


class DetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = PatientSerializer

    def get_object(self):
        firstname = self.kwargs.get('firstname')
        
        try:
            obj = Patient.objects.get(firstname=firstname)
            return obj
        except Patient.DoesNotExist:
            raise Http404('No patient matches the given name.')
        except Patient.MultipleObjectsReturned:
            raise Http404('Multiple patients found with the same name.')
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        except Patient.MultipleObjectsReturned:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        
        try:
            patient_info_update = self.get_object()
        except Http404:
            pass
        except Patient.MultipleObjectsReturned:
            pass
        
        serializer = PatientSerializer(instance=patient_info_update, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class IdDelete(RetrieveDestroyAPIView):
    
    serializer_class = PatientSerializer

    def get_object(self):
        id  = self.kwargs.get('id')
        try:
            obj = Patient.objects.get(id=id)
            
            return obj
        except Patient.DoesNotExist:
            raise Http404('No patient matches the given name.')
        except Patient.MultipleObjectsReturned:
            raise Http404('Multiple patients found with the same name')

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        except Patient.MultipleObjectsReturned:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)