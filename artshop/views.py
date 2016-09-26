from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ItemDetails

# Create your views here.
class ArtshopListView (TemplateView):
	template_name = "artshop_landing.html"

	def get(self, request,*args,**kwargs):
		context = super(ArtshopListView, self).get_context_data(**kwargs)
		context["all_itemdetails"] = ItemDetails.objects.all()
		return self.render_to_response(context)


class ItemDetailsView (TemplateView):
	template_name = "item_details.html"

	def get(self, request,*args,**kwargs):
		context = super(ItemDetailsView, self).get_context_data(**kwargs)
		context["item_details"] = ItemDetails.objects.get(id=context["item_id"])
		return self.render_to_response(context)