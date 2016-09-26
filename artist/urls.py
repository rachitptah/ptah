from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^landing/$', views.ArtistsLandingView.as_view(), name="artists_landing"),
    url(r'^landing/artist_id/(?P<artist_id>[0-9]+)$', views.ArtistProfileView.as_view(), name="artist_profile"),
    ]