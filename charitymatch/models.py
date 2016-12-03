from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    media_path = "charitymatch/organisations/image"
    upload_path = "{}/static/charitymatch/organisations/image".format("charitymatch")

    image = models.ImageField(upload_to=upload_path, default=None, null=True)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Category)

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

