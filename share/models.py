from django.db import models

# Create your models here.

class Shareboards(models.Model):
	name = models.CharField(max_length=200)

	def _unicode_(self):
		return self.name

class MarkedItems(object):
	"""docstring for MarkedItems"""
	name = models.CharField(max_length=200)
	comments= models.CharField(max_length=200)
	ratings = models.CharField(max_length=255)
	decision= models.BooleanField(default=1)

	def _unicode_(self):
		return self.name