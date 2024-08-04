from django.core import validators
from django.db import models
from django.db.models import Count


class CustomModelManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.annotate(number_of_articles=Count('articles')).order_by('-number_of_articles', 'email')


class Author(models.Model):
    full_name = models.CharField(max_length=100,
                                 validators=[validators.MinLengthValidator(3),
                                             validators.MaxLengthValidator(100)])

    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[validators.MinValueValidator(1900),
                                                         validators.MaxValueValidator(2005)])
    website = models.URLField(null=True)
    objects = CustomModelManager()


class Article(models.Model):
    CATEGORIES = [
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Education', 'Education')
    ]

    title = models.CharField(max_length=200, validators=[validators.MinLengthValidator(5),
                                                         validators.MaxLengthValidator(200)])
    content = models.TextField(validators=[validators.MinLengthValidator(10)])
    category = models.CharField(max_length=10, default='Technology', choices=CATEGORIES,
                                validators=[validators.MaxLengthValidator(10)])
    authors = models.ManyToManyField(Author, related_name='articles')
    published_on = models.DateTimeField(editable=False, auto_now_add=True)


class Review(models.Model):
    content = models.TextField(validators=[validators.MinLengthValidator(10)])
    rating = models.FloatField(validators=[validators.MinValueValidator(1.0), validators.MaxValueValidator(5.0)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='reviews')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')
    published_on = models.DateTimeField(auto_now_add=True, editable=False)