import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Order


# Import your models here
# Create and run your queries within functions


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(email__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
    ).order_by(
        'full_name'
    )

    return '\n'.join(
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}"
        for p in profiles
    )


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    return '\n'.join(
        f"Profile: {p.full_name}, orders: {p.orders.count()}" for p in profiles
    )


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ""

    product_names = [product.name for product in last_order.products.all()]

    return f"Last sold products: {', '.join(product_names)}"


def get_top_products():
    pass

