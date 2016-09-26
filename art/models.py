from __future__ import unicode_literals

from django.db import models

class ArtForm(models.Model): 
	name = models.CharField(max_length=250, blank=False)
	# enabled = models.BooleanField(default=False, help_text='Check To Enable A Category')

	def __unicode__(self):
		return self.name

class ArtType(models.Model):
	art_form = models.ForeignKey(ArtForm, on_delete=models.CASCADE)
	name = models.CharField(max_length=250, blank=False)

	def __unicode__(self):
		return self.name


	# def __init__(self, arg):
	# 	super(art-type, self).__init__()
	# 	self.arg = arg
		