from django.db import models


class Temoignage(models.Model):
    
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
