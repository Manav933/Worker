from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def getattribute(obj, attr):
    """Gets an attribute of an object dynamically from a string name"""
    try:
        return getattr(obj, attr)
    except (AttributeError, TypeError):
        return None

@register.filter
def get_errors(field):
    """Gets errors from a form field"""
    if hasattr(field, 'errors'):
        return field.errors
    return None

@register.filter
def add(value, arg):
    """Adds the arg to the value"""
    try:
        return value + str(arg)
    except (ValueError, TypeError):
        return value

@register.filter
def split(value, arg):
    """Splits a string by the given delimiter"""
    return value.split(arg) 