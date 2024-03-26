from django.urls import path
from . import views


app_name = 'insurances'


urlpatterns = [
    path('insurances/', views.InsurancesListCreate.as_view(), name='insurance-list-create'),
    path('insurances/<int:pk>/', views.InsurancesRetrieveUpdateDestroy.as_view(), name='insurance-retrieve-update-destroy'),
    path('insurance/', views.insurance, name='insurance'),
   
    
]



