from django import template
from posts.models import *

register = template.Library()


@register.simple_tag()
def get_days():
    return Day.objects.all()


@register.simple_tag()
def get_obj():
    return Object.objects.all()

@register.simple_tag()
def get_mes():
    return Messages.objects.all()