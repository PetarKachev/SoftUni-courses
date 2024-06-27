import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ChessPlayer, Meal, Dungeon, Workout, ArtworkGallery, Laptop


def show_highest_rated_art():
    arts = ArtworkGallery.objects.order_by('-rating', 'id')
    first_art = arts.first()
    return f"{first_art.art_name} is the highest-rated art with a {first_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    list_of_arts = [
        first_art,
        second_art
    ]
    ArtworkGallery.objects.bulk_create(list_of_arts)


def delete_negative_rated_arts():
    negative_ratings = ArtworkGallery.objects.filter(rating__lt=0)
    negative_ratings.delete()


def show_the_most_expensive_laptop():
    laptops = Laptop.objects.order_by('-price', '-id')
    first_laptop = laptops.first()

    return f"{first_laptop.brand} is the most expensive laptop available for {first_laptop.price}$!"


def bulk_create_laptops(args):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    laptops = Laptop.objects.all()

    for laptop in laptops:
        if laptop.brand == 'Asus' or laptop.brand == 'Lenovo':
            laptop.storage = 512
            laptop.save()


def update_to_16_GB_memory():
    laptops = Laptop.objects.all()

    for laptop in laptops:
        if laptop.brand == 'Apple' or laptop.brand == 'Dell' or laptop.brand == 'Acer':
            laptop.memory = 16
            laptop.save()


def update_operation_systems():
    laptops = Laptop.objects.all()

    for laptop in laptops:

        if laptop.brand == 'Asus':
            laptop.operation_system = 'Windows'
            laptop.save()

        elif laptop.brand == 'Apple':
            laptop.operation_system = 'MacOS'
            laptop.save()

        elif laptop.brand == 'Dell':
            laptop.operation_system = 'Linux'
            laptop.save()

        elif laptop.brand == 'Acer':
            laptop.operation_system = 'Linux'
            laptop.save()

        elif laptop.brand == 'Lenovo':
            laptop.operation_system = 'Chrome OS'
            laptop.save()


def delete_inexpensive_laptops():
    laptops = Laptop.objects.all()

    for laptop in laptops:
        if laptop.price < 1200:
            laptop.delete()
            laptop.save()