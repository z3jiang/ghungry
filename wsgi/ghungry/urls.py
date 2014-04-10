from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cafe/(.*)', 'ghungry.views.get_cafe'),
    url(r'^cafes', 'ghungry.views.get_cafes'),
)
