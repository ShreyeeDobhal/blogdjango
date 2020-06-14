import urllib
from django import template

register=template.Library()

@register.filter
def urlify(value):
    return urllib.parse.quote(value)

