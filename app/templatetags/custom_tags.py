from django import template

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