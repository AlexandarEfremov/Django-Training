from django import forms

from world_of_speed.cars.models import Car


class BaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(BaseForm):
    class Meta(BaseForm.Meta):
        fields = [
            "type",
            "model",
            "year",
            "image_url",
            "price",
        ]

        widgets = {
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
        }