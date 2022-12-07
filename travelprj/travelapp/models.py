from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pic")
    desc = models.TextField()
    
    
    def __str__(self):
        return self.name
    
class Peoples(models.Model):
    names = models.CharField(max_length=100)
    images = models.ImageField(upload_to="pic")
    descs = models.TextField()
    
    
    def __str__(self):
        return self.names