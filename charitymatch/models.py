from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name

