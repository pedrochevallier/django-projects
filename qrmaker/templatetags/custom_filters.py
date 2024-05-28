from django import template
from django.utils.encoding import force_bytes
import base64

register = template.Library()

@register.filter
def b64encode(value):
    if value:
        return base64.b64encode(force_bytes(value)).decode('ascii')
    else:
        return ''