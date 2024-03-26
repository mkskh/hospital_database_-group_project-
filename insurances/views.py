from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from .serializers import InsurancesSerializer
from .models import Insurances

from rest_framework import status
from rest_framework.response import Response


import requests


class InsurancesListCreate(generics.ListCreateAPIView):
    queryset = Insurances.objects.all()
    serializer_class = InsurancesSerializer
    
    
    
    
class InsurancesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insurances.objects.all()
    serializer_class = InsurancesSerializer
    
    
    

"""
def insurance(request):

    url = "http://127.0.0.1:8000/insurances/"
  

    if request.method == "GET":
        response = requests.get(url).json()
        return render(request, 'insurances/index.html')"""


def insurance(request):

    url2 = "http://127.0.0.1:8000/insurances/insurances/"
    response2 = requests.get(url2)
    insurances = response2.json()[:5]

    """if response.status_code == 200:
        data = response.json()[:5]
    else:
        print("Error:", response.status_code)"""

    return render(request, 'insurances/index.html', {'insurances': insurances})






    
    

    
    
    



    


    
    
    
    
  
    
    