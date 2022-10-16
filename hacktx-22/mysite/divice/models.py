from django.db import models

# Create your models here.

class NameItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ImageItem(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return "image: " + str(self.id)