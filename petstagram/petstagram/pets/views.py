from django.shortcuts import render, redirect
from .models import Pet
from ..photos.models import Photo
from .forms import PetForm, PetDeleteForm
from ..common.forms import CommentForm


def pet_add_page(request):
    form = PetForm(request.POST or None)
    comment_form = CommentForm()

    if form.is_valid():
        form.save()
        return redirect('profile-details-page', pk=1)#this is a random number for now
    context ={
        "form": form,
        "comment_form": comment_form
    }
    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        "pet": pet,
        "all_photos": all_photos,
        "comment_form": comment_form
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet-details-page", username, pet_slug)

    context = {
        "form": form
    }

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect("profile-details-page", pk=1)
    form = PetDeleteForm(instance=pet, initial=pet.__dict__)
    context = {
        "form": form
    }
    return render(request, template_name='pets/pet-delete-page.html', context=context)