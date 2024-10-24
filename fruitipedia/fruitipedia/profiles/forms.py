from django import forms

from fruitipedia.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        fields = "__all__"


class CreateProfileForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First Name"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last Name"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email"
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Password"
                }
            ),

        }

        labels ={
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": "",
        }


class EditProfileForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "image_url",
            "age"
        ]

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "image_url": "Image URL",
            "age": "Age",
        }