from django.db import models


class ProfileManager(models.Manager):

    def get_regular_customers(self):
        return self.annotate(
            number_of_orders=models.Count('orders')
        ).filter(
            number_of_orders__gt=2
        ).order_by('-number_of_orders')