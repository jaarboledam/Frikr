from django.core.exceptions import ValidationError

BADWORDS = ("meapilas", "aparcabicis", "tuercebotas", "abollao", "abrazafarolas", "afinabanjos", "diseñata")


def badwords(description):
    """
    Valida que la descripción no contenfa ninguna palabrota
    :return: diccionario con los datos limpios y validados
    """
    for badword in BADWORDS:
        if badword in description:
            raise ValidationError("La palabra {0} no está permitida".format(badword))
    return True