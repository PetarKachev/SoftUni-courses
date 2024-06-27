import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location


def create_pet(name: str, dog: str):
    Pet1 = Pet(
        name=name,
        species=dog
    )
    Pet1.save()

    return f"{Pet1.name} is a very cute {Pet1.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact1 = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    Artifact1.save()

    return f"The artifact {Artifact1.name} is {Artifact1.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    all_info = []
    all_locations = Location.objects.all().order_by('-id')

    for location in all_locations:
        all_info.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(all_info)


def new_capital():
    first_object = Location.objects.first()
    first_object.is_capital = True
    first_object.save()


def get_capitals():
    names = Location.objects.filter(is_capital=True).values('name')
    return names


def delete_first_location():
    return Location.objects.first().delete()