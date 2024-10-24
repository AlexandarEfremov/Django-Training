from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.profiles.validators import name_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            name_validator # TODO: test lower letter
        ]
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            name_validator # TODO: test lower letter
        ]
    )
    email = models.EmailField(
        unique=True,
        max_length=40,
    )

    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8)
        ],# TODO this help text is on the bottom of the field but it should be switched
        help_text="*Password length requirements: 8 to 20 characters"
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
    )

