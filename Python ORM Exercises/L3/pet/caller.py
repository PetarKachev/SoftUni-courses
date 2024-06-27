import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet


def create_pet(name: str, dog: str):
    Pet1 = Pet(
        name=name,
        species=dog
    )
    Pet1.save()

    return f"{Pet1.name} is a very cute {Pet1.species}!"