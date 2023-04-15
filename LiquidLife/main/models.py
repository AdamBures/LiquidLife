from django.db import models

# Create your models here.
class Filter(models.Model):
	name = models.CharField(max_length=30)
	icon = models.ImageField(upload_to ='static/images/')
	description = models.TextField()
	filtration_capacity = models.CharField(max_length=30)
	filtration_rate = models.CharField(max_length=30)
	micron_rating = models.CharField(max_length=30)
	lifespan = models.CharField(max_length=30)
