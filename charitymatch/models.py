from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    categorys = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name

