from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    dese=models.TextField()


    def __str__(self):
        return self.name

class Animal(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    dese=models.TextField()
    kg=models.TextField()