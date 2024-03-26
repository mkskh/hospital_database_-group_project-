from rest_framework import serializers

from .models import Insurances


class InsurancesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Insurances
        fields = "__all__"
        
        
        
    