from django import template
from contact.models import Social, About


register = template.Library()


@register.simple_tag()
def get_social_links():
    """Parinktis nuorodų soc. tinklų"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Parinktis about"""
    return About.objects.last()