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
    laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"


def bulk_create_laptops(args):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand='Asus').update(operation_system='Windows')
    Laptop.objects.filter(brand='Apple').update(operation_system='MacOS')
    Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='Linux')
    Laptop.objects.filter(brand='Lenovo').update(operation_system='Chrome OS')


def delete_inexpensive_laptops():
    Laptop.objects.filter(price_lt=1200).delete()


def bulk_create_chess_players(args):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if chess_player.title == 'no title':
            chess_player.delete()


def change_chess_games_won():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if chess_player.title == 'GM':
            chess_player.games_won = 30
            chess_player.save()


def change_chess_games_lost():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if chess_player.title == 'no title':
            chess_player.games_lost = 25
            chess_player.save()


def change_chess_games_drawn():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        chess_player.games_drawn = 10
        chess_player.save()


def grand_chess_title_GM():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if chess_player.rating >= 2400:
            chess_player.title = 'GM'
            chess_player.save()


def grand_chess_title_IM():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if 2300 <= chess_player.rating <= 2399:
            chess_player.title = 'IM'
            chess_player.save()


def grand_chess_title_FM():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if 2200 <= chess_player.rating <= 2299:
            chess_player.title = 'FM'
            chess_player.save()


def grand_chess_title_regular_player():
    chess_players = ChessPlayer.objects.all()

    for chess_player in chess_players:
        if 0 <= chess_player.rating <= 2199:
            chess_player.title = 'regular player'
            chess_player.save()