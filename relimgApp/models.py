# coding: utf-8

from django.db import models
from django.conf import settings

# Create your models here.
class Anime(models.Model):
	CONDITION_ANIME = (
		('E', 'En emisión'),
		('F', 'Finalizado'),
	)
	TYPE_ANIME = (
		('O', 'OVA'),
		('F', 'Película'),
		('A', 'Anime'),
	)
	title = models.CharField(max_length=255,default='')
	condition = models.CharField(max_length=1, choices=CONDITION_ANIME)
	type_anime = models.CharField(max_length=1, choices=TYPE_ANIME)
	description = models.CharField(max_length=10000,default='',blank=True,null=True)
	image_media = models.ImageField(upload_to=settings.STATIC_URL_IMAGE,max_length=255,blank=True,null=True)
	image_BD = models.CharField(max_length=255,default='',blank=True,null=True)
	date = models.DateTimeField('date')

	def __str__(self):
		return "%s" % self.title

	def save(self, *args, **kwargs):
		if  self.image_media:
			nombre = self.image_media.url.split('/')[-1]
			self.image_BD = nombre
		super(Anime, self).save(*args, **kwargs)

class Categorie(models.Model):
	anime = models.ForeignKey(Anime)
	categories = models.CharField(max_length=255,default='')
	date = models.DateTimeField('date')

	def __str__(self):
		return "%s" % self.anime

