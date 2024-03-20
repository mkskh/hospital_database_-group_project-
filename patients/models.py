from typing import Iterable
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
# Create your models here.



class Patient(models.Model):
    # GENDER_CHOICES = [
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('D', 'Diverse'),
    #     ('N', 'Non-Binary'),
    #     ('P', 'Prefer not to say'),
    #     ('O', 'Other'),  
    # ]
    
    DEPARTMENT_CHOICES = [
    ('CARD', 'Cardiology'),
    ('NEUR', 'Neurology'),
    ('ORTH', 'Orthopedics'),
    ('PEDI', 'Pediatrics'),
    ('DERM', 'Dermatology'),
    ('EMER', 'Emergency Medicine'),
    ('OBGY', 'Obstetrics and Gynecology'),
    ('ONCO', 'Oncology'),
    ('PSYC', 'Psychiatry'),
    ('ENDO', 'Endocrinology'),
    ('GAST', 'Gastroenterology'),
    ('UROL', 'Urology'),
    ('PULM', 'Pulmonology'),
    ('INF', 'Infectious Diseases'),
    ('RHEU', 'Rheumatology'),
    ('HEMA', 'Hematology'),
    ('NEPH', 'Nephrology'),
    ('ALLI', 'Allergy and Immunology'),
    ('GERI', 'Geriatrics'),
    ('OPHT', 'Ophthalmology'),
    ('OTOL', 'Otolaryngology'),
    ('PLAS', 'Plastic Surgery'),
    ('REHA', 'Rehabilitation Medicine'),
    ('NEON', 'Neonatology'),
    ('SPME', 'Sports Medicine'),
    ('PATH', 'Pathology'),
    ('RADI', 'Radiology'),
    ('ANES', 'Anesthesiology'),
    ('PHTH', 'Physical Therapy'),
    ('DENT', 'Dentistry'),
    ] 
    
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    maidenname = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = PhoneNumberField(unique=True)
    birthdate = models.DateField()
    profile_photo = models.ImageField(upload_to='patient_images', default= 'img/default.jpg')
    bloodgroup = models.CharField(max_length=10)
    height = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    eyecolor = models.CharField(max_length=10)
    medical_history = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    appointment = models.DateField(null=True, blank=True)
    department = models.CharField(choices= DEPARTMENT_CHOICES,max_length=50)
    
    def clean(self):
        if self.height > 999 or self.age > 999:
            raise ValidationError('Height or age can contain a maximum of 3 digits.')
        if self.height <= 0 or self.age <= 0 or self.weight <= 0:
            raise ValidationError('Height, weight or age should be greater then 0.')
    
    def __str__(self) -> str:
        return self.firstname