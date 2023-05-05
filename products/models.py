from django.db import models

from sorl.thumbnail import ImageField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    image = ImageField()



    def __str__(self):
        return self.title



