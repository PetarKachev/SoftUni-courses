import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import (Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense,
                             Car, Owner, Registration)

from datetime import date, timedelta


def show_all_authors_with_their_books() -> str:
    authors_with_books = []

    authors = Author.objects.all().order_by('id')

    for a in authors:
        books = Book.objects.filter(author=a)

        if not books:
            continue

        titles = ', '.join(b.title for b in books)
        authors_with_books.append(f"{a.name} has written - {titles}!")

    return '\n'.join(authors_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()
    # Django checks if our author's id is in books


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    avg_rating = sum(r.rating for r in reviews) / len(reviews)
    return avg_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    products = Product.objects.all()
    return products.filter(reviews__isnull=True).order_by('-name')
    # We use related_name here - 'reviews'


def delete_products_without_reviews():
    products_without_reviews = get_products_with_no_reviews()
    products_without_reviews.delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by('-license_number')

    return '\n'.join(str(lic) for lic in licenses)


def get_drivers_with_expired_licenses(due_date: date):
    expiration_cutoff_date = due_date - timedelta(days=365)
    # For a license to be considered valid it needs to be issued at minimum on this date

    drivers_with_expired_licenses = Driver.objects.filter(
        license__issue_date__gt=expiration_cutoff_date
    )

    return drivers_with_expired_licenses


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.save()
    # We cannot save the registration through the car

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return (f"Successfully registered {car.model} to "
            f"{owner.name} with "
            f"registration number {registration.registration_number}.")