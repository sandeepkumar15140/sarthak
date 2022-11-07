from django.db import models

# Create your models here.


class Product(models.Model):
    captions = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
