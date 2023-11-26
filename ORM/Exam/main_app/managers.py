from django.db import models


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.annotate(
            number_of_articles=models.Count('articles')
        ).order_by(
            '-number_of_articles',
            'email'
        )
