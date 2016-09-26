from django.conf import settings 
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^artivists/', include('artivists.urls')),
    # url(r'^signup',TemplateView.as_view(template_name="signup.html")),
    url(r'^artivities/', include('artivities.urls')),
    url(r'^artists/', include('artist.urls')),
    url(r'^artshop/', include('artshop.urls')),
    url(r'^home',TemplateView.as_view(template_name="home.html"), name='home'),
   
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)