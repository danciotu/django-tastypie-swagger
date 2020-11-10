try:
    from django.conf.urls import url, include
except (ImportError, ModuleNotFoundError):
    from django.conf.urls.defaults import include, url

from .views import SwaggerView, ResourcesView, SchemaView, Schema2View, SwaggerSpecs2View

app_name = 'tastypie_swagger'

urlpatterns = [
    url(r'^$', SwaggerView.as_view(), name='index'),
    url(r'^resources/$', ResourcesView.as_view(), name='resources'),
    url(r'^specs/(swagger.json)?$', SwaggerSpecs2View.as_view(), name='specs'),
    url(r'^specs/(?P<resource>\S+)/$', Schema2View.as_view()),
    url(r'^schema/(?P<resource>\S+)/$', SchemaView.as_view()),
    url(r'^schema/$', SchemaView.as_view(), name='schema'),
]
