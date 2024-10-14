from django.shortcuts import render, redirect
from .models import Pet
from ..photos.models import Photo
from .forms import PetForm


def pet_add_page(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details-page', pk=1)#this is a random number for now
    context ={
        "form": form
    }
    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        "pet": pet,
        "all_photos": all_photos
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit_page(request, username, pet_slug):
    return render(request, template_name='pets/pet-edit-page.html')


def pet_delete_page(request, username, pet_slug):
    return render(request, template_name='pets/pet-delete-page.html')