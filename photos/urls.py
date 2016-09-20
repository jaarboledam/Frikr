from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView
from photos.api import PhotoViewSet

router = DefaultRouter()
router.register('api/1.0/photos', PhotoViewSet, base_name='api_photos_')

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/(?P<pk>\d+)$', PhotoDetailView.as_view(), name='photos_detail'),  # ?P<nombre_parametro>
    url(r'^photos$', PhotoListView.as_view(), name='photos_my_photos'),

    # API URLS
    url(r'', include(router.urls))
]
