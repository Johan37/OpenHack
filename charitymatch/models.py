from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to="charitymatch/static/charitymatch/organisations/image", default=None, null=True)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Category)

    @property
    def get_name(self):
        return self.image.url.split('/')[-1]

    def __str__(self):
        return self.name

