import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order


# Create and run your queries within functions


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = (
         Q(full_name__icontains=search_string)
            |
         Q(email__icontains=search_string)
            |
         Q(phone_number__icontains=search_string)
    )

    profiles = Profile.objects.filter(query).order_by('full_name')

    if not profiles:
        return ""

    result = [
        f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}'
        for p in profiles
    ]

    return '\n'.join(result)


def get_loyal_profiles():

    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    result = [
        f'Profile: {p.full_name}, orders: {p.number_of_orders}'
        for p in profiles
    ]

    return '\n'.join(result)


def get_last_sold_products():
    last_order = Order.objects.all().last()

    if not last_order:
        return ""

    products = ', '.join([p.name for p in last_order.products.all()])

    return f'Last sold products: {products}'



