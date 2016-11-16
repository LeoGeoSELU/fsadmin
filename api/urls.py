from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'basescore', views.BaseScoreViewSet)

urlpatterns = [
    url(r'^sourcelist/$', views.datalist, name="sourcelist"),
    url(r'^sourcelist/(?P<source_id>[0-9]+)$', views.datacall, name="datacall"),
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
