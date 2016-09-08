from django.db import models

class Photo(models.Model):

    LICENCIAS = (
        ('RIG', 'CopyRight'),
        ('LEF', 'CopyLeft'),
        ('CC', 'Creative Commons')
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    license = models.CharField(max_length=3, choices=LICENCIAS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)