from django.db import models
class profile(models.Model):
	name = models.CharField(max_length=120)
	description =models.CharField(max_length=120)
	def __unicode__(self):
		return self.name

# Create your models here.
