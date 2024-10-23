from django.shortcuts import render, redirect

from django.shortcuts import render

from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile
from my_music_app.web.forms import CreateProfileForm


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "web/home-no-profile.html", context=context)

def index(request):
    profile = get_profile()
    if profile is None:
        return create_profile(request)

    albums = Album.objects.all()

    context = {
        "albums": albums
    }
    return render(request, "web/home-with-profile.html", context=context)


