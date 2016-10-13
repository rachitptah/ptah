from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Workshop
from artist.models import ArtistProfile
from art.models	import ArtForm, ArtType

# Create your views here.
class WorkshopListView (TemplateView):
	template_name = "artivities_home.html"

	def get(self, request,*args,**kwargs):
		context = super(WorkshopListView, self).get_context_data(**kwargs)
		art_form = request.GET.get("art_form","")
		art_type = request.GET.get("art_type","")
		filter_query_form = {}
		if art_form:
			filter_query_form["art_form_id"] = art_form

		context["art_types"] = ArtType.objects.filter(**filter_query_form)

		if art_type:
			filter_query_form["art_type_id"] = art_type
		filter_query_form["enable"]= True
		context["all_workshop"] = Workshop.objects.filter(**filter_query_form)
		context["art_forms"] = ArtForm.objects.all() 
		context["art_form"] = art_form
		return self.render_to_response(context)


class WorkshopDetailView (TemplateView):
	template_name = "workshop_details.html"

	def get(self, request,*args,**kwargs):
		context = super(WorkshopDetailView, self).get_context_data(**kwargs)
		context["workshop_detail"] = Workshop.objects.get(id=context["workshop_id"])
		
		return self.render_to_response(context)


	