from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, UpdateView, DeleteView
from my_music_app.albums.forms import AddAlbumForm
from my_music_app.albums.models import Album
from my_music_app.web.views import get_profile


class AddAlbumView(CreateView):
    model = Album
    form_class = AddAlbumForm
    template_name = "album/album-add.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    template_name = "album/album-details.html"
    context_object_name = "album"


class AlbumEditPage(UpdateView):
    model = Album
    form_class = AddAlbumForm
    template_name = "album/album-edit.html"
    success_url = reverse_lazy("index")


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = "album/album-delete.html"
    context_object_name = "album"
    success_url = reverse_lazy("index")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        form = AddAlbumForm(instance=album)
        for field in form.fields.values():
            field.disabled = True  # Disable fields so they cannot be edited
        context['form'] = form  # Pass the form into the context
        return context





