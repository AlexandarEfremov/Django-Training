from django.core.validators import MinLengthValidator
from django.db import models

from furry_funnies.core.validators import validate_first_name, validate_password


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            validate_first_name
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            validate_first_name
        ]
    )
    passcode = models.CharField(
        max_length=6,
        validators=[
            MinLengthValidator(6),
            validate_password
        ],
    )
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(
        null=True,
        blank=True
    )
    image_url = models.URLField(
        null=True,
        blank=True
    )