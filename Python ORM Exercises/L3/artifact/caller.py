import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact


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
