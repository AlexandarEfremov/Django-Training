from django import forms

from world_of_speed.profiles.models import Profile


class BaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseForm):
    class Meta(BaseForm.Meta):
        fields = [
            "username",
            "email",
            "age",
            "password",
        ]

        widgets = {
            "password": forms.PasswordInput(),
        }


class ProfileDetailsForm(BaseForm):
    class Meta(BaseForm.Meta):
        labels ={
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "profile_picture": "Profile Picture:"
        }