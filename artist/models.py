from __future__ import unicode_literals

from django.db import models
from art.models import ArtForm, ArtType

# Create your models here.

class ArtistProfile(models.Model):

	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

	name = models.CharField(max_length=100, blank=False, null=True)
	artist_type = models.CharField(max_length=100, blank=False, null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
	mobile_no = models.CharField(max_length=10, blank=True, null=True, help_text='Please enter mobile number without +91 or 0')
	art_form = models.ForeignKey(ArtForm, null=True, on_delete=models.CASCADE)
	art_type = models.ForeignKey(ArtType, null=True, on_delete=models.CASCADE, verbose_name="Art Type")
	about_yourself = models.TextField(max_length=500, blank=True, null=True)
	avatar = models.ImageField (upload_to="artists_avatar/", blank=True, null=True)
	cover_image = models.ImageField (upload_to="artists_cover_image/", blank=True, null=True)
	dob = models.DateField(null=True)

	@property
	def avatar_url(self):
	    if self.avatar and hasattr(self.avatar, 'url'):
	        return self.avatar.url

	@property
	def cover_url(self):
	    if self.cover_image and hasattr(self.cover_image, 'url'):
	        return self.cover_image.url



	def __unicode__(self):
		return self.name