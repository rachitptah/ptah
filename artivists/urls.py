from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.UserFormView.as_view(), name="Signup"),
    url(r'^login/$', views.UserLoginView.as_view(), name="Login"),
    url(r'^logout/$', views.UserLogoutView.as_view(), name="Logout"),
]