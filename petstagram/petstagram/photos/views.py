from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoCreateForm


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

    context ={
        "photo": photo,
        "likes": likes,
        "comments": comments,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit_page(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')