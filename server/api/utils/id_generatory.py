from django.utils.http import int_to_base36
import uuid
ID_LENGTH = 40


def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)
