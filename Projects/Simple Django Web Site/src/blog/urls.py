from django.urls import path
from .views import index, article_01, article_02, article_03

urlpatterns = [
    path('', index, name="blog-index"),
    path("article_01/", article_01, name="blog-article-01"),
    path("article_02/", article_02, name="blog-article-02"),
    path("article_03/", article_03, name="blog-article-03"),
]