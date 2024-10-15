from django import forms
from ..photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        form = Photo
        fields = "__all__"

