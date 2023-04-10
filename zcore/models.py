from django.db import models

# write a model for an image
class Image(models.Model):
	image = models.ImageField(upload_to='images/')
	caption = models.CharField(max_length=100)

	def __str__(self):
		return self.caption