from django.core.exceptions import ValidationError


def letter_validation(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')

