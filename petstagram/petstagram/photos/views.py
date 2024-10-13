from django.shortcuts import render
from .models import Photo


def photo_add_page(request):
    return render(request, template_name='photos/photo-add-page.html')


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