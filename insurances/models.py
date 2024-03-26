from django.db import models


class Insurances(models.Model):
    TYPE_COMPANY_CHOICES = [
        ('PRIVATE', 'Private'),
        ('PUBLIC', 'Public'),
    ]

    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    type_company = models.CharField(max_length=30, choices=TYPE_COMPANY_CHOICES)
    

    def __str__(self):
        return f"{self.company_name}"
    
