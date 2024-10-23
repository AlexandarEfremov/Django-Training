from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.profiles.models import Profile


class Album(models.Model):
    class GenreChoices(models.TextChoices):
        POP = "Pop Music", "Pop Music"
        JAZZ = "Jazz Music", "Jazz Music"
        RNB = "R&B Music", "R&B Music"
        ROCK = "Rock Music", "Rock Music"
        COUNTRY = "Country Music", "Country Music"
        DANCE = "Dance Music", "Dance Music"
        HIP_HOP = "Hip Hop Music", "Hip Hop Music"
        OTHER = "Other", "Other"

    album_name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=30,
        # verbose_name="Album Name"
    )
    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30
    )
    genre = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        choices=GenreChoices.choices
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0.0)
        ]
    )
    owner = models.ForeignKey(
        to=Profile,
        # TODO: Check foreign key
        on_delete=models.CASCADE,
    )
