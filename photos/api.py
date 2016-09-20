from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotoQueryset


class PhotoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('name', 'description')
    order_fields = ('owner', 'created_at', 'name', 'id')
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return PhotoQueryset.get_photos_by_user(self.request.user)

    def get_serializer_class(self):
        return PhotoSerializer if self.action != 'list' else PhotoListSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
