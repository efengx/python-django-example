from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'trip/list/(?P<pk>[0-9]+)/$', views.trip_list),
    url(r'trailer/$', views.TrailerList.as_view()),
    url(r'trailer/(?P<pk>[0-9]+)/$', views.TrailerDetail.as_view()),
    url(r'trip/(?P<pk>[0-9]+)/$', views.VehiclesDetail.as_view()),
    url(r'trip/list/$', views.VehicleList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
