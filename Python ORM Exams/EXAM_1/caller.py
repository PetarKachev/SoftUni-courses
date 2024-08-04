import os
import django
from django.db.models import Q, Count, Avg, F

from main_app.models import Director, Actor, Movie

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def get_directors(search_name: str = None, search_nationality: str = None):
    if search_name is None and search_nationality is None:
        return ''

    elif search_name is not None and search_nationality is not None:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
        directors = Director.objects.filter(query).order_by('full_name')

        if not directors:
            return ''

        return '\n'.join(
            [f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}" for d in
             directors])

    elif search_name is not None and search_nationality is None:
        query = Q(full_name__icontains=search_name)
        directors = Director.objects.filter(query).order_by('full_name')

        if not directors:
            return ''

        return '\n'.join(
            [f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}" for d in
             directors])

    elif search_name is None and search_nationality is not None:
        query = Q(nationality__icontains=search_nationality)
        directors = Director.objects.filter(query).order_by('full_name')

        if not directors:
            return ''

        return '\n'.join(
            [f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}" for d in
             directors])


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ''

    return f"Top Director: {director.full_name}, movies: {director.number_of_movies}."


def get_top_actor():
    top_actor = Actor.objects.prefetch_related('starring_actor_movies').annotate(
        number_of_movies=Count('starring_actor_movies'), average_rating=Avg('starring_actor_movies__rating')).order_by(
        '-number_of_movies', 'full_name').first()

    if not top_actor or not top_actor.number_of_movies:
        return ''

    titles = ', '.join(movie.title for movie in top_actor.starring_actor_movies.all() if movie)

    return f"Top Actor: {top_actor.full_name}, starring in movies: {titles}, movies average rating: {top_actor.average_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(number_of_movies=Count('actors_movies')).order_by('-number_of_movies', 'full_name')[
             :3]

    if not actors or not actors[0].number_of_movies:
        return ''

    result = []

    for a in actors:
        result.append(f"{a.full_name}, participated in {a.number_of_movies} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    movie = Movie.objects.select_related('starring_actor').prefetch_related('actors').filter(is_awarded=True).order_by(
        '-rating', 'title').first()

    if not movie:
        return ''

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    actor_full_names = ', '.join([actor.full_name for actor in movie.actors.all().order_by('full_name')])

    return f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. Starring actor: {starring_actor}. Cast: {actor_full_names}."


def increase_rating():
    movies = Movie.objects.all().filter(is_classic=True, rating__lt=10.0)

    if not movies:
        return "No ratings increased."

    updated_movies = movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies} movies."