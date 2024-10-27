from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furry_funnies.author.forms import AuthorBaseForm, AuthorProfileCreateForm, AuthorEditForm
from furry_funnies.author.models import Author
from furry_funnies.core.utils import get_profile


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorProfileCreateForm
    template_name = "author/create-author.html"
    success_url = reverse_lazy("dashboard")


class AuthorDetailsView(DetailView):
    model = Author
    template_name = "author/details-author.html"
    context_object_name = "author"

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['last_post_title'] = author.post_set.last().title if author.post_set.exists() else "N/A"
        return context


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = "author/edit-author.html"
    success_url = reverse_lazy("author_details")

    def get_object(self, queryset=None):
        return get_profile()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author/delete-author.html"
    context_object_name = "author"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()


