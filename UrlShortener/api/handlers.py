from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from api.models import Url
from api.utils import generate_random_string
from api.exception import CantRewriteExistingUrlError, UnknownUrlError


def add_new_url(long_url: str) -> str:
    try:
        return Url.objects.create(long_url=long_url, short_url=generate_random_string()).short_url
    except IntegrityError:
        raise CantRewriteExistingUrlError


def get_real_url(short_url: str) -> str:
    try:
        url = Url.objects.get(short_url=short_url)
        return url.long_url
    except ObjectDoesNotExist:
        raise UnknownUrlError
