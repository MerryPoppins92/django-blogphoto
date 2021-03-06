from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	description1 = models.CharField(max_length = 1000)
	date = models.DateField()
	image = models.ImageField(upload_to = 'blog/images/')

# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(max_length=1000)
#     slug = models.SlugField(max_length=40)

class Blogbuster(models.Model):
	title = models.CharField(max_length = 100)
	description1 = models.CharField(max_length = 1000)
	date = models.DateField()
	image1 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image2 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image3 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image4 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image5 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image6 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image7 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image8 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image9 = models.ImageField(upload_to = 'blog/images/', blank = True)
	image0 = models.ImageField(upload_to = 'blog/images/', blank = True)
	slug = models.SlugField(max_length=40)

	def __str__(self):
		return self.title

