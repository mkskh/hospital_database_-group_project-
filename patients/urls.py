from django.urls import path
from . import views


app_name = 'patients'

urlpatterns = [
    path('', views.PatientView.as_view(), name='patient'),
    path('<str:firstname>/', views.DetailUpdateDeleteView.as_view(), name='details'),
    path('id_delete/<int:id>/', views.IdDelete.as_view(), name='id_delete'),
]