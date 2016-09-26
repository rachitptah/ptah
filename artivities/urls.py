from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.WorkshopListView.as_view(), name="artivities_home"),
    url(r'^workshop_id/(?P<workshop_id>[0-9]+)$', views.WorkshopDetailView.as_view(), name="workshop_details"),
    ]