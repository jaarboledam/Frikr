from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotoQueryset


class PhotoListAPI(ListCreateAPIView):
    """
    Endpoint de listado y creacion de fotos
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PhotoQueryset.get_photos_by_user(self.request.user)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle, actualizacion y borrado de fotos
    """
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PhotoQueryset.get_photos_by_user(self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
