from django.db import models

# Create your models here.
class Post(models.Model):
    class Metta:
        vebose_name = "Post"
        verbose_name_plural = "qiymatlar"

    nomi = models.CharField(max_length=256)
    #qiymati = models.TextField()
    daromadqiymati = models.IntegerField()

    def __str__(self):
        return self.nomi