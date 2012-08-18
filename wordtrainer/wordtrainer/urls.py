from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import trainer_site.urls

admin.autodiscover()
urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(trainer_site.urls))
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

