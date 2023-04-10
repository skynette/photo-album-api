from django.db import models
import cloudinary.models

class Image(cloudinary.models.CloudinaryResource):
    caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.caption
