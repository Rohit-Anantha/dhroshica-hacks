from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return "image: " + str(self.id)

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)