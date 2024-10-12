from django.shortcuts import render


def pet_add_page(request):
    return render(request, template_name='pets/pet-add-page.html')


def pet_details_page(request, username, pet_slug):
    return render(request, template_name='pets/pet-details-page.html')


def pet_edit_page(request, username, pet_slug):
    return render(request, template_name='pets/pet-edit-page.html')


def pet_delete_page(request, username, pet_slug):
    return render(request, template_name='pets/pet-delete-page.html')