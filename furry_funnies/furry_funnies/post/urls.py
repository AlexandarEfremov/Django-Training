from django.urls import include, path

from furry_funnies.post import views
from furry_funnies.post.views import CreatePostView, DetailsPostView, EditPostView, DeletePostView

urlpatterns=[
    path('create/', CreatePostView.as_view(), name='post_create'),
    path('<int:pk>/', include([
        path('details/', DetailsPostView.as_view(), name='post_details'),
        path('edit/', EditPostView.as_view(), name='post_edit'),
        path('delete/', DeletePostView.as_view(), name='post_delete')
    ]))
]
