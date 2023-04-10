from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
	image = CloudinaryField('image')
	caption = models.CharField(max_length=100)
	
	def __str__(self):
		return self.caption