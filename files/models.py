from django.db import models

# Create your models here.

class File(models.Model):

    url = models.FileField(upload_to="uploads")
    name = models.CharField(max_length=250)