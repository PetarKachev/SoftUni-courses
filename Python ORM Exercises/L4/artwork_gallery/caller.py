import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ChessPlayer, Meal, Dungeon, Workout, ArtworkGallery


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
