from django import forms
from ..photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user']


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ["photo"]