from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^cafes', 'ghungry.views.list_cafes'),
    url(r'^menu/(.*)', 'ghungry.views.get_menu_by_cafe'),
)
