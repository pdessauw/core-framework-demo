from django.conf.urls import include, url
from django.contrib import admin

import test_views


urlpatterns = [
    url(r'^test$', test_views.template_test, name="test"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("core_website.urls")),
]
