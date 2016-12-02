from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to="charitymatch/static/charitymatch/organisations/image", default=None, null=True)
    # image = models.ImageField(upload_to = "organisation/image", default =  None, null=True)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name

