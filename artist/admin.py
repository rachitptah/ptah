from django.contrib import admin
from .models import	ArtistProfile
from .forms import ArtistForm

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
	
	form = ArtistForm

admin.site.register(ArtistProfile, ArtistAdmin)
