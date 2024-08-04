import os
import django
from django.db.models import Q, Count, Avg, F

from main_app.models import Author, Article, Review

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def get_authors(search_name: str = None, search_email: str = None):
    if search_name is None and search_email is None:
        return ''

    elif search_name is not None and search_email is not None:
        query = Q(full_name__icontains=search_name) & Q(email__icontains=search_email)

        authors = Author.objects.filter(query).order_by('-full_name')

        if not authors:
            return ''

        result = []

        for author in authors:
            result.append(
                f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}")

        return '\n'.join(result)

    elif search_name is not None and search_email is None:
        query = Q(full_name__icontains=search_name)

        authors = Author.objects.filter(query).order_by('-full_name')

        if not authors:
            return ''

        result = []

        for author in authors:
            result.append(
                f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}")

        return '\n'.join(result)

    elif search_name is None and search_email is not None:
        query = Q(email__icontains=search_email)

        authors = Author.objects.filter(query).order_by('-full_name')

        if not authors:
            return ''

        result = []

        for author in authors:
            result.append(
                f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}")

        return '\n'.join(result)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()
    if top_author is None or top_author.number_of_articles == 0:
        return ''

    return f"Top Author: {top_author.full_name} with {top_author.number_of_articles} published articles."


def get_top_reviewer():
    top_author = Author.objects.annotate(number_of_reviews=Count('reviews')).order_by('-number_of_reviews',
                                                                                      'email').first()

    if top_author is None or top_author.number_of_reviews == 0:
        return ''

    return f"Top Reviewer: {top_author.full_name} with {top_author.number_of_reviews} published reviews."


def get_latest_article():
    if not Article.objects.all():
        return ''

    article = Article.objects.prefetch_related('authors', 'reviews').order_by('-published_on').first()
    if not article:
        return ''

    authors_fullnames = ', '.join([article.full_name for article in article.authors.all().order_by('full_name')])
    num_reviews = article.reviews.count()
    avg_rating = sum([review.rating for review in article.reviews.all()]) / num_reviews if num_reviews else 0.0

    return f"The latest article is: {article.title}. " \
           f"Authors: {authors_fullnames}. " \
           f"Reviewed: {num_reviews} times. " \
           f"Average Rating: {avg_rating:.2f}."


def get_top_rated_article():
    top_rated_article = Article.objects.\
                         annotate(avg_rating=Avg('reviews__rating')).\
                         order_by('-avg_rating', 'title').\
                         first()

    num_reviews = top_rated_article.reviews.count() if top_rated_article else 0
    if top_rated_article is None or num_reviews == 0:
        return ''

    avg_rating = top_rated_article.avg_rating or 0.0
    return (f"The top-rated article is: {top_rated_article.title}, "
            f"with an average rating of {avg_rating:.2f}, "
            f"reviewed {num_reviews} times.")


def ban_author(email: str = None):
    if email is None or not Author.objects.all():
        return "No authors banned."

    author = Author.objects.prefetch_related('reviews').filter(email__exact=email).first()

    if not author:
        return "No authors banned."

    author.is_banned = True
    author.save()
    count_of_reviews = author.reviews.count()
    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {count_of_reviews} reviews deleted."