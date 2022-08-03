from tabnanny import verbose
from django.db import models

class Post(models.Model):
    class Metta:
        verbose_name = "Post"
        verbose_name = "Postlar"
    nomi = models.CharField(max_length=256)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.nomi 