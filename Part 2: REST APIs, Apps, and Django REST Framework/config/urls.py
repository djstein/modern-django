from django.conf.urls import include, url
from django.contrib import admin
from project import api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('project.api.urls')),
]
