from django.shortcuts import render
from django.views.generic import ListView

from furry_funnies.core.utils import get_profile
from furry_funnies.post.models import Post


def index(request):
    author = get_profile()
    posts = Post.objects.all()
    context = {
        'author': author,
        'posts': posts,
    }
    return render(request, 'web/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'web/dashboard.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_profile()
        return context

