from django.shortcuts import render

# Create your views here.
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from files.models import File


class FileSerializer(ModelSerializer):

    class Meta:
        model = File


class FileViewSet(ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer

