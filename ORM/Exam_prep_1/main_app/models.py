from django.db import models
from django.core import validators
from main_app.managers import DirectorManager

from main_app.validators import validate_positive


class Person(models.Model):
    full_name = models.CharField(
        max_length=120, 
        validators=[validators.MinLengthValidator(2)]
    )

    birth_date = models.DateField(
        default='1900-01-01'
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )

    class Meta:
        abstract = True


class Awarded_Updated(models.Model):

    is_awarded = models.BooleanField(
        default=False
    )

    last_updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Director(Person):

    years_of_experience = models.SmallIntegerField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    def __str__(self):
        return self.full_name
    
    objects = DirectorManager()


class Actor(Person, Awarded_Updated):

    def __str__(self):
        return self.full_name


class Movie(Awarded_Updated):

    GENRES_CHOICES = (
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        max_length=150,
        validators=[validators.MinLengthValidator(5)]
    )

    release_date = models.DateField()

    storyline = models.TextField(
        null=True,
        blank=True
    )

    genre = models.CharField(
        max_length=6,
        default='Other',
        choices=GENRES_CHOICES
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[validators.MinValueValidator(0.0), validators.MaxValueValidator(10.0)],
        default=0.0
    )

    is_classic = models.BooleanField(
        default=False
    )

    director = models.ForeignKey(
        to=Director, 
        on_delete=models.CASCADE,
        related_name='director_movies'
    )

    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        related_name='starring_movies',
        null=True,
        blank=True
    )

    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
    

    

