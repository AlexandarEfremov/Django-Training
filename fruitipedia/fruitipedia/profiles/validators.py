from django.core.exceptions import ValidationError


def name_validator(value):
    if not value[0].isalpha():
        return ValidationError('Your name must start with a letter!')
