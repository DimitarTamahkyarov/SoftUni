import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Director, Movie
from django.db import models
from django.db.models import Avg, Q, F


# Create and run your queries within functions

def get_directors(search_name=None, search_nationality=None):

    query = ''

    if search_name is not None and search_nationality is not None:

        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)

    elif search_name is None:
        query = Q(nationality__icontains=search_nationality)

    elif search_nationality is None:
        query = Q(full_name__icontains=search_name)

    directors = Director.objects.filter(query).order_by('full_name')

    if directors:
        return '\n'.join(
            f'Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}' 
            for d in directors
        )
    
    return ''

def get_top_director():

    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ''

    return f'Top Director: {director.full_name}, movies: {director.number_of_movies}.'

def get_top_actor():

    actor = Actor.objects.annotate(
        number_of_movies=models.Count('starring_movies'),
        avg_rating=models.Avg('starring_movies__rating'),
    ).order_by(
        '-number_of_movies', 
        'full_name'
    ).first()

    if not actor or not actor.number_of_movies:
        return ''
    
    movies = Movie.objects.filter(starring_actor=actor)

    return f'Top Actor: {actor.full_name}, starring in movies: {", ".join(movie.title for movie in actor.starring_movies.all())}, movies average rating: {actor.avg_rating:.1f}'

def get_actors_by_movies_count():

    actors = Actor.objects.annotate(
        number_of_movie=models.Count('movie')
    ).order_by(
        '-number_of_movie',
        'full_name'
    )[:3]

    if not actors or actors[0].number_of_movie == 0:
        return ''
    
    result = [
        f"{actor.full_name}, participated in {actor.number_of_movie} movies"
        for actor in actors
    ]

    return '\n'.join(result)

def get_top_rated_awarded_movie():

    movie = Movie.objects.filter(
        is_awarded=True,
    ).order_by(
        '-rating',
        'title',
    ).first()

    if not movie:
        return ''
    
    starring_actor = movie.starring_actor.full_name

    if not starring_actor:
        starring_actor = 'N/A'

    actors = ', '.join(movie.actors.all().order_by('full_name').values_list('full_name', flat=True))
    
    return f"Top rated awarded movie: {movie.title}, rating: {movie.rating}. Starring actor: {starring_actor}. Cast: {actors}."

def increase_rating():
    updated_movies = Movie.objects.filter(
        is_classic=True,
        rating__lte=9.9
    ).update(
        rating=F('rating') + 0.1
    )

    if not updated_movies:
        return "No ratings increased."
    
    return f"Rating increased for {len(updated_movies)} movies."

