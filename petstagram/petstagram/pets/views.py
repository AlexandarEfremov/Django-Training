from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Pet
from ..photos.models import Photo
from .forms import PetForm, PetDeleteForm
from ..common.forms import CommentForm


class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details-page', kwargs={"pk": 1})


#model = Pet: Specifies the model that the view is associated with, in this case, the Pet model.

#form_class = PetForm: Specifies the form class to be used for handling input data. In this context, it's set to
# PetForm, the form class associated with the Pet model.

#template_name = 'pets/pet-add-page.html': Specifies the template file that will be used to render the HTML content
# for this view. The template is located at 'pets/pet-add-page.html'.
# success_url = reverse_lazy('profile-details', kwargs={'pk': 1}): Specifies the URL to redirect to after a successful
# form submission. In this case, it uses reverse_lazy to dynamically generate the URL for the 'profile-details' view
# with a specific primary key (pk=1). The use of reverse_lazy allows for resolving the URL at runtime


# def pet_add_page(request):
#     form = PetForm(request.POST or None)
#     comment_form = CommentForm()
#
#     if form.is_valid():
#         form.save()
#         return redirect('profile-details-page', pk=1)#this is a random number for now
#     context ={
#         "form": form,
#         "comment_form": comment_form
#     }
#     return render(request, template_name='pets/pet-add-page.html', context=context)


class PetDetailsView(DetailView):
    model = Pet
    template_name = "pets/pet-details-page.html"
    context_object_name = "pet"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_photos"] = self.object.photo_set.all()
        context["comment_form"] = CommentForm()
        return context

    #context_object_name = 'pet': Assigns the name 'pet' to the object retrieved from the database,
    # making it accessible in the template

    #slug_url_kwarg = 'pet_slug': Captures the pet's slug from the URL and passes it as a keyword argument to the view.

    #The get_context_data method is overridden to enhance the context with additional data:
    #context['all_photos']: Retrieves all photos related to the pet using the reverse relation photo_set.
    #context['comment_form']: Includes a new instance of the CommentForm to handle comment


# def pet_details_page(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         "pet": pet,
#         "all_photos": all_photos,
#         "comment_form": comment_form
#     }
#     return render(request, template_name='pets/pet-details-page.html', context=context)


class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"
    context_object_name = "pet"

    def get_success_url(self):
        return reverse_lazy("pet-details-page", kwargs={
            "username": self.kwargs["username"],
            "pet_slug": self.kwargs["pet_slug"]
        })

#· In the example code provided, the get_success_url method is overridden to customize the redirect URL.

#· The reverse_lazy function is used to dynamically generate the URL based on the pet-details URL pattern.
# The kwargs parameter allows you to pass dynamic values to the URL pattern.

#· In this case, it constructs the URL using the username and pet_slug from the current instance's kwargs.

# def pet_edit_page(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     if request.method == "GET":
#         form = PetForm(instance=pet, initial=pet.__dict__)
#     else:
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect("pet-details-page", username, pet_slug)
#
#     context = {
#         "form": form
#     }
#
#     return render(request, template_name='pets/pet-edit-page.html', context=context)


class DeletePetView(DeleteView):
    model = Pet
    template_name = "pets/pet-delete-page.html"
    context_object_name = "pet"
    success_url = reverse_lazy("profile-details-page", kwargs={"pk": 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs["pet_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PetDeleteForm(initial=self.object.__dict__)

    def delete(self, request, *args, **kwargs):
        pet=self.get_object()
        pet.delete()
        return redirect(self.success_url)

# In the DeletePetView class-based view, several methods are overridden to customize the behavior of the view.
# Here's an explanation of each method:
#
# · get_queryset(self):
    # o This method is used to return the queryset of objects that the DeleteView operates on.
    #
    # o In the DeletePetView, it is overridden to filter the queryset based on the pet_slug from the URL parameters.
    #
    # o This method helps define which set of objects can be deleted. In this case, it ensures that only the specific
    # Pet object with the given slug can be deleted.
#
# · delete(self, request, *args, **kwargs):
#
    # o In the DeletePetView, it uses the get_object method to retrieve the specific Pet object to be deleted.
    #
    # o After retrieving the object, it calls the delete method on the object to remove it from the database.
    #
    # o Finally, it redirects the user to the specified success_url, which, in this case, is the 'profile-details' page.





# def pet_delete_page(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     if request.method == "POST":
#         pet.delete()
#         return redirect("profile-details-page", pk=1)
#     form = PetDeleteForm(instance=pet, initial=pet.__dict__)
#     context = {
#         "form": form
#     }
#     return render(request, template_name='pets/pet-delete-page.html', context=context)
