from __future__ import unicode_literals

from django.db import models
from art.models import ArtForm, ArtType
from artist.models import ArtistProfile

# Create your models here.
class ItemDetails (models.Model):
	item_name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Item Name")
	artform = models.ForeignKey(ArtForm, null=True, on_delete=models.CASCADE, verbose_name="Art Form")
	arttype = models.ForeignKey(ArtType, null=True, on_delete=models.CASCADE, verbose_name="Art Type")
	is_artist = models.ForeignKey(ArtistProfile, null=True, on_delete=models.CASCADE, verbose_name="Artist")
	description = models.TextField(max_length=500, blank=False, null=True)
	item_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	item_image = models.ImageField (upload_to="art_shop/", blank=False, null=True)
	created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
	modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

	def __unicode__(self):
		return self.item_name

	@property
	def item_image_url(self):
	    if self.item_image and hasattr(self.item_image, 'url'):
	        return self.item_image.url

