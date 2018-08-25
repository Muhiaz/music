from django.db import models

class album(models.Model):
	artist = models.CharField(max_length=120)
	album_tittle = models.CharField(max_length=120)
	genre = models.CharField(max_length=120)
	album_logo = models.ImageField(max_length=120,null =True,blank =True)

	def __unicode__(self):
		return self.artist


class song(models.Model):
	artist = models.CharField(max_length=120)
	song_tittle = models.CharField(max_length=120)
	genre = models.CharField(max_length=120)
	def __unicode__(self):
		return self.artist

# Create your models here.
