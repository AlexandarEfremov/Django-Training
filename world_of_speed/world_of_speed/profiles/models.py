from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.profiles.validators import validate_username


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, "Username must be at least 3 chars long!"),
            validate_username
        ]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators= [
            MinValueValidator(21)
        ],
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(
        max_length=20
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def total_car_price(self):
        return sum(car.price for car in self.car_set.all())