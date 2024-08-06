from django.core import validators
from django.db import models
from django.db.models import Count


class CustomModelManager(models.Manager):
    def get_tennis_players_by_wins_count(self):
        return self.annotate(number_of_wins=Count('winner_matches')).order_by('-number_of_wins', 'full_name')


class TennisPlayer(models.Model):
    full_name = models.CharField(max_length=120, validators=[validators.MinLengthValidator(5),
                                                             validators.MaxLengthValidator(120)])
    birth_date = models.DateField()
    country = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2),
                                                           validators.MaxLengthValidator(100)])
    ranking = models.PositiveIntegerField(validators=[validators.MinValueValidator(1),
                                                      validators.MaxValueValidator(300)])
    is_active = models.BooleanField(default=True)
    objects = CustomModelManager()


class Tournament(models.Model):
    SURFACE_TYPES = [
        ('Not Selected', 'Not Selected'),
        ('Clay', 'Clay'),
        ('Grass', 'Grass'),
        ('Hard Court', 'Hard Court')
    ]

    name = models.CharField(max_length=150, unique=True, validators=[validators.MinLengthValidator(2),
                                                                     validators.MaxLengthValidator(150)])
    location = models.CharField(max_length=100, validators=[validators.MinLengthValidator(2),
                                                            validators.MaxLengthValidator(100)])
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    surface_type = models.CharField(max_length=12, default='Not Selected', choices=SURFACE_TYPES,
                                    validators=[validators.MaxLengthValidator(12)])


class Match(models.Model):
    score = models.CharField(max_length=100, validators=[validators.MaxLengthValidator(100)])
    summary = models.TextField(validators=[validators.MinLengthValidator(5)])
    date_played = models.DateTimeField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_matches')
    players = models.ManyToManyField(TennisPlayer, related_name='players_matches')
    winner = models.ForeignKey(TennisPlayer, on_delete=models.SET_NULL, null=True, related_name='winner_matches')

    class Meta:
        verbose_name_plural = 'Matches'