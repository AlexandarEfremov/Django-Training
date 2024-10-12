from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, template_name='accounts/register-page.html')


def login():
    return None


def profile_details_page():
    return None


def profile_edit_page():
    return None


def profile_delete_page():
    return None