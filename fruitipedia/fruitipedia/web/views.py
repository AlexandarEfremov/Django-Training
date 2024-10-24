from django.shortcuts import render
from django.views.generic import ListView

from fruitipedia.fruits.models import Fruit
from fruitipedia.profiles.models import Profile


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist:
        return None
def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request, 'web/index.html', context=context)


def dashboard(request):
    profile = get_profile()
    fruits = Fruit.objects.all()
    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'web/dashboard.html', context=context)
