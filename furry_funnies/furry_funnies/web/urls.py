from django.urls import path

from furry_funnies.web import views
from furry_funnies.web.views import PostListView

urlpatterns=[
    path('', views.index, name='index'),
    path('dashboard/', PostListView.as_view(), name='dashboard')
]
