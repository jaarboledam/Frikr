from photos.models import Photo
from django.forms import ModelForm


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        # fields = ['visibility', etc...] // aquí se puede indicar los campos del modelo que se deben rederizar
        exclude = ['owner']  # aquí se indican los campos del modelo que no se deben incluir
