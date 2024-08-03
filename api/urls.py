from django.urls import path
from .views import ArtistViewSet, AlbomViewSet, SongViewSet

urlpatterns = [
    path('artist/', ArtistViewSet.as_view(), name='artist-list'),
    path('artist/<int:id>/', ArtistViewSet.as_view(), name='artist-detail'),

    path('albom/', AlbomViewSet.as_view(), name='albom-list'),
    path('albom/<int:id>/', AlbomViewSet.as_view(), name='albom-detail'),

    path('songs/', SongViewSet.as_view(), name='song-list'),
    path('songs/<int:id>/', SongViewSet.as_view(), name='song-detail'),
]
