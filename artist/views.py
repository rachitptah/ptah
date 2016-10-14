from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ArtistProfile
from art.models	import ArtForm, ArtType
from artivities.models import Workshop

# Create your views here.
class ArtistsLandingView (TemplateView):
	template_name = "artists_landing.html"

	def get(self, request,*args,**kwargs):
		context = super(ArtistsLandingView, self).get_context_data(**kwargs)
		art_form = request.GET.get("art_form","")
		art_type = request.GET.get("art_type","")
		filter_query_form = {}
		if art_form:
			filter_query_form["art_form_id"] = art_form

		context["art_types"] = ArtType.objects.filter(**filter_query_form)

		if art_type:
			filter_query_form["art_type_id"] = art_type
		context["all_artists"] = ArtistProfile.objects.filter(**filter_query_form)
		context["art_forms"] = ArtForm.objects.all() 
		context["art_form"] = art_form
		return self.render_to_response(context)
		


class ArtistProfileView (TemplateView):
	template_name = "artist_profile.html"

	def get(self, request,*args,**kwargs):
		context = super(ArtistProfileView, self).get_context_data(**kwargs)
		context["artist_profiles"] = ArtistProfile.objects.get(id=context["artist_id"])
		context["artist_workshops"] = Workshop.objects.filter(artist_id=context["artist_id"])
		return self.render_to_response(context)