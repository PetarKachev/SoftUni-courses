from django.core.exceptions import ValidationError
from django.db import models
from datetime import date


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        years = int(str(date.today())[:4]) - int(str(self.birth_date)[:4])
        month_todays_date = int(str(date.today())[5:7])
        month_birth_date = int(str(self.birth_date)[5:7])
        day_todays_date = int(str(date.today())[8:])
        day_birth_date = int(str(self.birth_date)[8:])

        if month_todays_date > month_birth_date:
            pass

        elif month_todays_date < month_birth_date:
            years -= 1

        elif month_todays_date == month_birth_date:

            if day_todays_date > day_birth_date:
                pass

            elif day_todays_date < day_birth_date:
                years -= 1

            elif day_todays_date == day_birth_date:
                pass

        return years


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    PREDEFINED_CHOISES = (
        ('Mammals', 'Mammals'),
        ('Birds', 'Birds'),
        ('Reptiles', 'Reptiles'),
        ('Others', 'Others')
    )
    specialty = models.CharField(max_length=10, choices=PREDEFINED_CHOISES)
    managed_animals = models.ManyToManyField(Animal)

    def clean(self):
        super().clean()

        choices = [choice[0] for choice in self.PREDEFINED_CHOISES]
        if self.specialty not in choices:
            raise ValidationError("Specialty must be a valid choice.")


class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = ((True, 'Available'), (False, 'Not Available'))
        kwargs['default'] = True
        super().__init__(*args, **kwargs)


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
    availability = BooleanChoiceField()


class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    def display_info(self):
        return f"Meet {self.name}! Species: {self.species}, born {self.birth_date}. It makes a noise like '{self.sound}'."

    def is_endangered(self):
        if self.species in ["Cross River Gorilla", "Orangutan", "Green Turtle"]:
            return f"{self.species} is at risk!"
        else:
            return f"{self.species} is not at risk."
