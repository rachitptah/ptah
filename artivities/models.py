from __future__ import unicode_literals
from geoposition.fields import GeopositionField

from django.db import models
from art.models import ArtForm, ArtType
from artist.models import ArtistProfile

# Create your models here.
class Venue(models.Model):
	venue_name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Venue Name")
	website = models.URLField(blank=True, null=True)
	address = GeopositionField()

	def __unicode__(self):
		return self.venue_name


class Workshop(models.Model):
	title = models.CharField(max_length=250, blank=False, null=True)
	art_form = models.ForeignKey(ArtForm, null=True, on_delete=models.CASCADE)
	art_type = models.ForeignKey(ArtType, null=True, on_delete=models.CASCADE, verbose_name="Art Type")
	description = models.TextField(max_length=1000, blank=False, null=True)
	artist = models.ForeignKey(ArtistProfile, null=True, on_delete=models.CASCADE)
	cover_photo = models.ImageField (upload_to="cards/", blank=False, null=True)
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	startdate = models.DateTimeField(null=True, verbose_name="Start Date/Time")
	enddate = models.DateTimeField(null=True, verbose_name="End Date/Time")
	total_seats = models.IntegerField(blank=False, null=True)
	enable = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title


class Registration(models.Model):	

	workshop = models.ForeignKey(Workshop, null=True, on_delete=models.CASCADE)
	regtype = models.CharField(max_length=100, blank=False, null=True, verbose_name="Registration Type")
	description = models.TextField(max_length=100, blank=True, null=True)
	quantity = models.IntegerField(blank=False, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	startdate = models.DateTimeField(null=True, verbose_name="Sale Start Date/Time")
	enddate = models.DateTimeField(null=True, verbose_name="Sale End Date/Time")
	addcharges = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	def __unicode__(self):
		return self.regtype

class Discount(models.Model):

	DISCOUNT_TYPE = (
        ('F', 'Flat'),
        ('P', 'Percentage'),
    )

	regtype = models.ForeignKey(Registration, null=True, on_delete=models.CASCADE, verbose_name="Registration Type")
	disctype = models.CharField(max_length=1, choices=DISCOUNT_TYPE, blank=True, null=True, verbose_name="Discount Type")
	discname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Discount Name")
	Discount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	startdate = models.DateTimeField(null=True, verbose_name="Start Date/Time")
	enddate = models.DateTimeField(null=True, verbose_name="End Date/Time")
	enable = models.BooleanField(default=False)
	def __unicode__ (self):
		return self.discname