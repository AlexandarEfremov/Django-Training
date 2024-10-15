from django.core.validators import MinLengthValidator
from django.db import models

from ..pets.models import Pet
from .validators import validate_field_size


class Photo(models.Model):
    photo = models.ImageField(
        upload_to="images",
        validators=[
            validate_field_size,
    ])
    description = models.TextField(
        blank=True,
        null=True,
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ]
    )
    location = models.CharField(
        max_length=30
    )
    tagged_pets = models.ManyToManyField(
        blank=True,
        to=Pet
    )
    date_of_publication = models.DateField(
        auto_now=True, #can be updated
    )
