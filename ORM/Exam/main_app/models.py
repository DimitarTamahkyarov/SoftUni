from django.core import validators
from django.db import models

from main_app.managers import AuthorManager


class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[validators.MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(1900), validators.MaxValueValidator(2005)]
    )
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()


class Published(models.Model):
    class Meta:
        abstract = True

    content = models.TextField(validators=[validators.MinLengthValidator(10)])
    published_on = models.DateTimeField(auto_now_add=True, editable=False)


class Article(Published):
    CATEGORIES = (
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Education', 'Education'),
    )

    title = models.CharField(max_length=200, validators=[validators.MinLengthValidator(5)])
    category = models.CharField(max_length=10, choices=CATEGORIES, default='Technology')
    authors = models.ManyToManyField(Author, related_name='articles')


class Review(Published):

    rating = models.FloatField(validators=[validators.MinValueValidator(1.0), validators.MaxValueValidator(5.0)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='reviews')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')

