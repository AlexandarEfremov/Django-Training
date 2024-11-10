from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoCreateForm, PhotoEditForm
from ..common.forms import CommentForm


def photo_add_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home-page")

    context = {
        "form": form
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)


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