from django.db import models

class Category(models.Model):
    media_path = "charitymatch/categories/image"
    upload_path = "{}/static/charitymatch/categories/image".format("charitymatch")

    ### Fields ###
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path, default=None, null=True, blank=True)
    image_text = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    media_path = "charitymatch/subcategories/image"
    upload_path = "{}/static/charitymatch/subcategories/image".format("charitymatch")

    ### Fields ###
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path, default=None, null=True, blank=True)
    image_text = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    regions = models.ManyToManyField(Region)

    def __str__(self):
        return self.name

class Method(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    media_path = "charitymatch/organisations/image"
    upload_path = "{}/static/charitymatch/organisations/image".format("charitymatch")

    image = models.ImageField(upload_to=upload_path, default=None, null=True, blank=True)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(SubCategory)
    regions = models.ManyToManyField(Region)
    methods = models.ManyToManyField(Method)

    @property
    def get_name(self):
        return self.image.url.split('/')[-1]

        # <img src="/static/charitymatch/organisations/image/{{organisation.get_name}}" width="100">

    @property
    def get_image_path(self):
        return "/static/{media_path}/{name}".format(media_path=self.media_path,
                                                    name=self.get_name)

    def __str__(self):
        return self.name

