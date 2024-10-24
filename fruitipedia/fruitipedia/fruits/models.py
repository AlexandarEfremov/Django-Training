from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.fruits.validators import letter_validation


def unique_validation(instance=None):
    def validate(value):
        if instance and Fruit.objects.filter(name=value).exclude(pk=instance.pk).exists():
            raise ValidationError('This fruit name is already in use! Try a new one.')
    return validate


class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            letter_validation,# TODO test letter validation
            unique_validation() #TODO test unique
        ]
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
    )
