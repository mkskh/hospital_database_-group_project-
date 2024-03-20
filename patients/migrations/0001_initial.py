# Generated by Django 5.0.3 on 2024-03-19 09:05

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=40)),
                ("lastname", models.CharField(max_length=40)),
                ("maidenname", models.CharField(max_length=40)),
                ("age", models.PositiveIntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("D", "Diverse"),
                            ("N", "Non-Binary"),
                            ("P", "Prefer not to say"),
                            ("O", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("birthdate", models.DateField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="patient_images"
                    ),
                ),
                ("bloodgroup", models.CharField(max_length=10)),
                ("height", models.SmallIntegerField()),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                ("eyecolor", models.CharField(max_length=10)),
                ("medical_history", models.TextField()),
                ("treatment", models.TextField()),
                ("appointment", models.DateField()),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("CARD", "Cardiology"),
                            ("NEUR", "Neurology"),
                            ("ORTH", "Orthopedics"),
                            ("PEDI", "Pediatrics"),
                            ("DERM", "Dermatology"),
                            ("EMER", "Emergency Medicine"),
                            ("OBGY", "Obstetrics and Gynecology"),
                            ("ONCO", "Oncology"),
                            ("PSYC", "Psychiatry"),
                            ("ENDO", "Endocrinology"),
                            ("GAST", "Gastroenterology"),
                            ("UROL", "Urology"),
                            ("PULM", "Pulmonology"),
                            ("INF", "Infectious Diseases"),
                            ("RHEU", "Rheumatology"),
                            ("HEMA", "Hematology"),
                            ("NEPH", "Nephrology"),
                            ("ALLI", "Allergy and Immunology"),
                            ("GERI", "Geriatrics"),
                            ("OPHT", "Ophthalmology"),
                            ("OTOL", "ENT (Otolaryngology)"),
                            ("PLAS", "Plastic Surgery"),
                            ("REHA", "Rehabilitation Medicine"),
                            ("NEON", "Neonatology"),
                            ("SPME", "Sports Medicine"),
                            ("PATH", "Pathology"),
                            ("RADI", "Radiology"),
                            ("ANES", "Anesthesiology"),
                            ("PHTH", "Physical Therapy"),
                            ("DENT", "Dentistry"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
