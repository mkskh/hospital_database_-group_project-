import django_filters
from .models import Patient


class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = {
            'age':['gte', 'lte'],
            'gender':['iexact'],
            'birthdate':['gte', 'lte'],
            'height' : ['gte', 'lte'],
            'weight': ['gte', 'lte'],
            'department': ['exact'],
            'eyecolor': ['iexact'],
        }