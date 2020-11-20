from django.db import models

class project(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	image = models.ImageField(upload_to = 'portfolio/images/')
	url = models.URLField(blank = True)
	slug = models.SlugField(max_length=40, blank = True, null = True)

	def __str__(self):
		return self.title

