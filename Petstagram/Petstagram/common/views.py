from django.shortcuts import render
from ..photos.models import Photo
from ..common.models import Like
from ..common.forms import CommentForm, SearchForm
from django.views.generic import ListView
from pyperclip import copy
from django.shortcuts import redirect, resolve_url


# Create your views here.
class HomePageView(ListView):
    model = Photo
    template_name = "common/home-page.html"
    context_object_name = "page_obj" #this tells django which is the name we want to use by default it's object_list
    paginate_by = 1

    def get_context_data(self, **kwargs): #this is how we can access the forms
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["search_form"] = SearchForm(self.request.GET) #so that the search request doesn't disappear
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get("pet_name")

        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)

        return queryset

def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url("photo-details-page", photo_id))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False) #we want to take the comment and relate it to the photo
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")