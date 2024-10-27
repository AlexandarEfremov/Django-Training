from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furry_funnies.core.utils import get_profile
from furry_funnies.post.forms import PostCreateForm, PostUpdateForm, PostBaseForm
from furry_funnies.post.models import Post

class AuthorContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #type: ignore
        context['author'] = get_profile()
        return context

class CreatePostView(AuthorContextMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/create-post.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.author_id = get_profile().pk
        return super().form_valid(form)



class DetailsPostView(AuthorContextMixin, DetailView):
    model = Post
    template_name = "post/details-post.html"
    context_object_name = "post"


class EditPostView(AuthorContextMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "post/edit-post.html"
    success_url = reverse_lazy("dashboard")


class DeletePostView(DeleteView):
    model = Post
    # form_class = PostDeleteForm
    template_name = "post/delete-post.html"
    context_object_name = "post"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        form = PostBaseForm(instance=post)
        for field in form.fields.values():
            field.disabled = True
        context['form'] = form
        context['author'] = get_profile()
        return context


