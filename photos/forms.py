from django.core.exceptions import ValidationError

from photos.models import Photo
from django.forms import ModelForm


BADWORDS = ("meapilas", "aparcabicis", "tuercebotas", "abollao", "abrazafarolas", "afinabanjos", "diseñata")

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        # fields = ['visibility', etc...] // aquí se puede indicar los campos del modelo que se deben rederizar
        exclude = ['owner']  # aquí se indican los campos del modelo que no se deben incluir

    def clean(self):
        """
        Valida que la descripción no contenfa ninguna palabrota
        :return: diccionario con los datos limpios y validados
        """
        cleaned_data = super().clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("La palabra {0} no está permitida".format(badword))
        return cleaned_data
