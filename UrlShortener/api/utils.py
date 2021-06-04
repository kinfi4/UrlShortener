from string import ascii_lowercase, digits
from random import choice


def generate_random_string(length=7):
    return ''.join(choice([*digits, *ascii_lowercase]) for _ in range(length))
