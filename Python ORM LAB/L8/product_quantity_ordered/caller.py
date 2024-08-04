import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from pprint import pprint
from main_app.models import Product
from django.db.models import Count, Sum, Max


def product_quantity_ordered():
    ordered_products = list(Product.objects.values('name').annotate(ordered_total_quantity=Sum('orderproduct__quantity')).order_by('-ordered_total_quantity'))
    result = []

    for product in ordered_products:
        if product['ordered_total_quantity'] is not None:
            result.append(f"Quantity ordered of {product['name']}: {product['ordered_total_quantity']}")

    return '\n'.join(result)

print(product_quantity_ordered())