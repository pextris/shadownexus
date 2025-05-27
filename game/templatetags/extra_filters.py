from django import template
register = template.Library()

@register.filter
def with_index(sequence):
    return list(enumerate(sequence))