from django.db import models

# Create your models here.

class Blog(models.Model):
	baslik = models.CharField(max_length=100)
	icerik = models.CharField(max_length=500)
	olusturulma_tarihi = models.DateTimeField()
