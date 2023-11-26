import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Article, Review
from django.db.models import Q, Count, Avg, Max


def get_authors(search_name=None, search_email=None):

    authors = None

    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(
            full_name__icontains=search_name,
            email__icontains=search_email
        ).order_by('-full_name')

    elif search_name is not None:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')

    elif search_email is not None:
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')

    if authors is None:
        return ''

    result = [
        f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}"
        for a in authors
    ]

    return '\n'.join(result)


def get_top_publisher():
    top_publisher = Author.objects.annotate(
        number_of_articles=Count('articles')
    ).filter(
        number_of_articles__gt=0
    ).order_by(
        '-number_of_articles',
        'email'
    ).first()

    if not top_publisher:
        return ''

    return f'Top Author: {top_publisher.full_name} with {top_publisher.number_of_articles} published articles.'


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(
        number_of_review=Count('reviews')
    ).filter(
        number_of_review__gt=0
    ).order_by(
        '-number_of_review',
        'email'
    ).first()

    if not top_reviewer:
        return ''

    return f'Top Reviewer: {top_reviewer.full_name} with {top_reviewer.number_of_review} published reviews.'


def get_latest_article():

    a = Article.objects.annotate(
        average_rating=Avg('reviews__rating')
    ).order_by('published_on').last()

    if a is None:
        return ''

    if a.average_rating is None:
        a.average_rating = 0

    authors = [author.full_name for author in a.authors.all().order_by('full_name')]

    return (f'The latest article is: {a.title}. Authors: {", ".join(authors)}'
            f'. Reviewed: {a.reviews.count()} times. Average Rating: {a.average_rating:.2f}.')


def get_top_rated_article():

    top_article = Article.objects.prefetch_related(
        'reviews'
    ).annotate(
        avg_reviews=Avg('reviews__rating')
    ).order_by(
        '-avg_reviews',
        'title'
    ).first()

    if top_article is None or top_article.avg_reviews is None:
        return ''

    return f'The top-rated article is: {top_article.title}, with an average rating of {top_article.avg_reviews:.2f}, '\
            f'reviewed {top_article.reviews.count()} times.'


def ban_author(email=None):

    if email is None:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if author is None:
        return "No authors banned."

    author.is_banned = True
    author.save()

    deleted_reviews = Review.objects.filter(author=author).delete()

    return f"Author: {author.full_name} is banned! {deleted_reviews[0]} reviews deleted."


print(get_latest_article())







