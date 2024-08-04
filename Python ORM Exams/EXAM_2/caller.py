import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, F

from main_app.models import Profile, Order, Product


def get_profiles(search_string: str = None):
    if search_string is None:
        return ''

    query = (Q(full_name__icontains=search_string) |
             Q(email__icontains=search_string) |
             Q(phone_number__icontains=search_string))

    profiles = Profile.objects.filter(query).order_by('full_name')

    return '\n'.join(
        [f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}"
         for p in profiles])


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    return '\n'.join([f"Profile: {p.full_name}, orders: {p.orders.count()}"
                      for p in profiles])


def get_last_sold_products():
    latest_order = Order.objects.prefetch_related('products').last()

    if latest_order is None or not latest_order.products.exists():
        return ''

    return f"Last sold products: {', '.join([p.name for p in latest_order.products.all()])}"


def get_top_products():
    most_sold_products = Product.objects.annotate(count_of_orders=Count('orders')).filter(count_of_orders__gt=0).order_by('-count_of_orders', 'name')[:5]

    if most_sold_products is None or not most_sold_products:
        return ''

    return f"Top products:\n" + '\n'.join([f'{p.name}, sold {p.orders.count()} times' for p in most_sold_products])


def apply_discounts():
    count_discounted_orders = Order.objects.annotate(count_of_products=Count('products')).filter(
        count_of_products__gt=2, is_completed=False).update(total_price=F('total_price') * 0.90)

    return f"Discount applied to {count_discounted_orders} orders."


def complete_order():
    oldest_order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if not oldest_order:
        return ''

    for product in oldest_order.products.all():

        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    oldest_order.is_completed = True
    oldest_order.save()
    return "Order has been completed!"
