from django.core import validators
from django.db import models
from django.db.models import Count


class CustomModelManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(number_of_movies=Count('director_movies')).order_by('-number_of_movies', 'full_name')


class Director(models.Model):
    full_name = models.CharField(max_length=120,
                                 validators=[validators.MinLengthValidator(2), validators.MaxLengthValidator(120)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown', validators=[validators.MaxLengthValidator(50)])
    years_of_experience = models.SmallIntegerField(default=0, validators=[validators.MinValueValidator(0)])
    objects = CustomModelManager()


class Actor(models.Model):
    full_name = models.CharField(max_length=120, validators=[validators.MinLengthValidator(2),
                                                             validators.MaxLengthValidator(120)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown', validators=[validators.MaxLengthValidator(50)])
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)


class Movie(models.Model):
    GENRES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other')
    ]

    title = models.CharField(max_length=150, validators=[validators.MinLengthValidator(5),
                                                         validators.MaxLengthValidator(150)])
    release_date = models.DateField()
    storyline = models.TextField(null=True)
    genre = models.CharField(max_length=6, default='Other', validators=[validators.MaxLengthValidator(6)], choices=GENRES)
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=1, validators=[validators.MinValueValidator(0.0),
                                                                                          validators.MaxValueValidator(10.0)])
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director_movies')
    starring_actor = models.ForeignKey(Actor, null=True, on_delete=models.SET_NULL, related_name='starring_actor_movies')
    actors = models.ManyToManyField(Actor, related_name='actors_movies')
