import os
import django
from datetime import date, timedelta, datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ZooKeeper, Veterinarian, Mammal, Animal, Reptile, Employee
