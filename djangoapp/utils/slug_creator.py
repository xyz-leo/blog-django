import string
from random import SystemRandom
from django.utils.text import slugify


def random_text(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))


def create_slug(text, k=3):
    return slugify(text) + '-' + random_text(k)
