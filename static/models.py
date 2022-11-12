from django.db import models

# Create your models here.


class Product(models.Model):
    captions = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.captions


class Users(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)


