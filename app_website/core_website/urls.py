from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_view, name="core_website_home"),
    url(r'^help$', views.help_view, name="core_website_help"),
]
