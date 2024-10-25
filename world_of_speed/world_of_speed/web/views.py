from django.shortcuts import render

from world_of_speed.profiles.models import Profile


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile:
        context = {
            'profile': profile,
        }
        return render(request, "web/index.html", context=context)
    return render(request, "web/index.html")

