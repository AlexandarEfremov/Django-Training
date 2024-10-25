from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.cars.validators import year_validator

"""
•	Car
o	Type
	Character (choice) field, required.
	It should consist of a maximum of 10 characters.
	The choices are "Rally", "Open-wheel", "Kart", "Drag" and "Other".
o	Model
	Character field, required.
	It should consist of a maximum of 15 characters.
	It should consist of a minimum of 1 characters.
o	Year
	Integer field, required.
	Valid year is a year between 1999 and 2030 (both inclusive). Otherwise, raise a ValidationError with the message: "Year must be between 1999 and 2030!"
o	Image URL
	URL field, required, unique.
	A placeholder: "https://..."
	A custom error message for unique constraint: "This image URL is already in use! Provide a new one."
o	Price
	Float field, required.
	Price cannot be below 1.0.	
o	Owner
	A foreign key to the Profile model.
	Establishes a many-to-one relationship with the Profile model, associating each car with a profile.
	The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
	This field should remain hidden in forms.

"""

class Car(models.Model):
    class CarChoices(models.TextChoices):
        RALLY = 'Rally', 'Rally'
        OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
        KART = 'Kart', 'Kart'
        DRAG = 'Drag', 'Drag'
        OTHER = 'Other', 'Other'

    type = models.CharField(
        max_length=10,
        choices=CarChoices.choices,
    )
    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )
    year = models.IntegerField(
        validators=[
            year_validator
        ]
    )
    image_url = models.URLField(
        unique=True,
        error_messages={
            "unique": "This image URL is already in use! Provide a new one."
        }
    )
    price = models.FloatField(
        validators= [
            MinValueValidator(1.0)
        ]
    )
    owner = models.ForeignKey(
        to="profiles.Profile",
        on_delete=models.CASCADE,
    )

