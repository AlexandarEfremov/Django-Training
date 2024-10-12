from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, template_name='accounts/register-page.html')


def login(request):
    return render(request, template_name='accounts/login-page.html')


def profile_details_page(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def profile_edit_page(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def profile_delete_page(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')