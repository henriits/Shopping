from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)


    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text



class Items(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    image = models.ImageField
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
