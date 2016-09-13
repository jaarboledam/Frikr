from django.conf.urls import url
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/(?P<pk>\d+)$', PhotoDetailView.as_view(), name='photos_detail'),  # ?P<nombre_parametro>
    url(r'^photos$', PhotoListView.as_view(), name='photos_my_photos'),
]
