from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_username(value):
    is_valid = all(ch.isalnum() or ch == '_' for ch in value)
    if not is_valid:
        raise ValidationError(
            "Ensure this value contains only letters, numbers, and underscore."
        )


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            validate_username

        ]
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )