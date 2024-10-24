"""
Template file: "create-fruit.html"
The page consists of:
•	A navigation bar, as shown below.
•	A fruit creation form consisting of:
	A "Name" field, a placeholder "Fruit Name" and no label
	An "Image URL" field, a placeholder "Fruit Image URL" and no label
	A "Description" field, a placeholder "Fruit Description" and no label
	A "Nutrition" field, a placeholder "Nutrition Info" and no label
•	A button "Add Fruit"
	When you click on it if the fruit is successfully created, you should be redirected to the dashboard page.
	Otherwise, the form should show the appropriate validation errors.
	Associate the new fruit post with the user profile you already have in the database.

"""
from django import forms
from django.core.validators import MinLengthValidator

from fruitipedia.fruits.models import Fruit, unique_validation
from fruitipedia.fruits.validators import letter_validation


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = [
            "name",
            "image_url",
            "description",
            "nutrition",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Fruit Name"
                }
            ),
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "Fruit Image URL"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Fruit Description"
                }
            ),
            "nutrition": forms.Textarea(
                attrs={
                    "placeholder": "Nutrition Info"
                }
            )
        }

        labels = {
            "name": "",
            "image_url": "",
            "description": "",
            "nutrition": "",
        }


class EditFruitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Check if the instance exists
            self.fields['name'].validators.append(unique_validation(self.instance))

    class Meta:
        model = Fruit
        fields = [
            "name",
            "image_url",
            "description",
            "nutrition",
        ]

        labels = {
            "name": "Name",
            "image_url": "Image URL",
            "description": "Description",
            "nutrition": "Nutrition",
        }


