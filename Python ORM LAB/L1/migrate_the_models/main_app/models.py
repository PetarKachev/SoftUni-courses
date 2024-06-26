from django.db import models
from datetime import datetime, date


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    SOFIA = 'Sofia'
    PLOVDIV = 'Plovidv'
    BURGAS = 'Burgas'
    VARNA = 'Varna'

    CITY_CHOISES = [
        (SOFIA, 'Sofia'),
        (PLOVDIV, 'Plovdiv'),
        (BURGAS, 'Burgas'),
        (VARNA, 'Varna')
    ]

    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(default=1, verbose_name="Employees Count")
    location = models.CharField(max_length=20, null=True, choices=CITY_CHOISES, blank=True)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)