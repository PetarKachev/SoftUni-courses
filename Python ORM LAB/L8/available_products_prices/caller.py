import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Product, Order
from django.db.models import Sum, Q


def product_quantity_ordered():
    ordered_products = list(
        Product.objects.values('name').annotate(ordered_total_quantity=Sum('orderproduct__quantity')).order_by(
            '-ordered_total_quantity'))
    result = []

    for product in ordered_products:
        if product['ordered_total_quantity'] is not None:
            result.append(f"Quantity ordered of {product['name']}: {product['ordered_total_quantity']}")

    return '\n'.join(result)


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related('orderproduct_set__product__category')
    result = []

    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")

        for current_order in order.orderproduct_set.all():
            result.append(f'- Product: {current_order.product.name}, Category: {current_order.product.category.name}')

    return '\n'.join(result)


def filter_products():
    query = Q(price__gt=3.00) & Q(is_available=True)
    products = Product.objects.filter(query).order_by('-price', 'name')
    result = []

    for product in products:
        result.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(result)