from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ArtshopListView.as_view(), name="artshop_landing"),
    url(r'^item_id/(?P<item_id>[0-9]+)$', views.ItemDetailsView.as_view(), name="item_details"),
    ]