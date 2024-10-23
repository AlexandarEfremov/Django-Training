from django.urls import path, include

from my_music_app.albums.views import AddAlbumView, AlbumDetailsView, AlbumEditPage, AlbumDeleteView

urlpatterns = [
    path('add/', AddAlbumView.as_view(), name='add_album'),
    path('<int:pk>', include([
        path('details/', AlbumDetailsView.as_view(), name='details_album'),
        path('edit/', AlbumEditPage.as_view(), name='edit_album'),
        path('delete/', AlbumDeleteView.as_view(), name='delete_album'),
    ]))
]