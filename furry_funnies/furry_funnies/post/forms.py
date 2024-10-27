from django import forms

from furry_funnies.post.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "image_url",
            "content",
        )

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Put an attractive and unique title..."
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Share some interesting facts about your adorable pets..."
                }
            )
        }

        labels = {
            "title": "Title:",
            "image_url": "Post Image URL:",
            "content": "Content:",
        }

        help_texts = {
            "image_url": "Share your funniest furry photo URL!"
        }

class PostCreateForm(PostBaseForm):
    pass

class PostUpdateForm(PostBaseForm):
    pass

# class PostDeleteForm(PostBaseForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for _, field in self.fields.items():
#             field.widget.attrs['disabled'] = "disabled"
#             field.widget.attrs['readonly'] = "readonly"
