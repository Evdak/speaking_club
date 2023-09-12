from django import template

register = template.Library()


@register.filter(name="iso_format_with_colon")
def iso_format_with_colon(value):
    return value.isoformat()
