from django.core.exceptions import ObjectDoesNotExist

from api.models import Url
from api.utils import generate_random_string
from api.exception import UnknownUrlError


def add_new_or_get_existing_url(long_url: str):
    obj, created = Url.objects.get_or_create(long_url=long_url)

    if created:
        obj.short_url = generate_random_string()
        obj.save()

    return obj, created


def get_real_url(short_url: str) -> str:
    try:
        url = Url.objects.get(short_url=short_url)
        return url.long_url
    except ObjectDoesNotExist:
        raise UnknownUrlError
