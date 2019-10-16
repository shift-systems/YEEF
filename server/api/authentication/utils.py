from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from api.utils.token import token_generator

from django.conf import settings
backend_domain = settings.BACKEND_DOMAIN


def generate_link(user_obj, route):
    token = token_generator.make_token(user_obj)
    uid = urlsafe_base64_encode(force_bytes(
        user_obj.id)).decode()

    link = f"{backend_domain}/{route}/{uid}/{token}"
    return link
