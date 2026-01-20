from django import template
from django.db import connection

register = template.Library()

@register.filter(name='upper_name')
def upper_name(value):
    return value.upper()

@register.simple_tag
def format_name(first, last):
    return f"{first} - {last}"

@register.inclusion_tag('components/card.html')
def card(title, year, poster):
    return {
        'title': title,
        'year': year,
        'poster': poster,
    }

@register.simple_tag
def multiply(first, last):
    return int(first) * int(last)

@register.filter
def currency_idr(value):
    try:
        value = int(value)
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value

@register.simple_tag
def get_total(price, qty):
    with connection.cursor() as cursor:
        cursor.execute("SELECT calculate_total(%s, %s)", [price, qty])
        total = cursor.fetchone()[0]
    return total