from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Photo
from .forms import PhotoCreateForm, PhotoEditForm
from ..common.forms import CommentForm


class PhotoAddPage(CreateView):
    model = Photo
    template_name = "photos/photo-add-page.html"
    form_class = PhotoCreateForm
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()

        form.save_m2m()
        return super().form_valid(form)


def photo_details_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "likes": likes,
        "comments": comments,
        "comment_form": comment_form
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("photo-details-page", pk)

    context = {
        "form": form,
        "photo": photo
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()

    return redirect("home-page")