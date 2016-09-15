from django.db import models
from django.contrib.auth.models import User

from photos.validators import badwords

LICENSE_COPYRIGHT = 'RIG'
LICENSE_COPYLEFT = 'LEF'
LICENSE_CC = 'CC'

LICENCIAS = (
    (LICENSE_COPYRIGHT, 'CopyRight'),
    (LICENSE_COPYLEFT, 'CopyLeft'),
    (LICENSE_CC, 'Creative Commons')
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)


class Photo(models.Model):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(null=True, blank=True, validators=[badwords])  # Permitir valores nulos y vacios
    license = models.CharField(max_length=3, choices=LICENCIAS, default=LICENSE_CC)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):  # mifoto.__str__()
        return self.name
