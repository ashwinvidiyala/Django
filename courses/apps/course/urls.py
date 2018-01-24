from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^course/$', views.index),
    url(r'^course/destroy_confirmation/(?P<id>\d+)', views.destroy_confirmation),
    url(r'^course/destroy/(?P<id>\d+)', views.destroy),
    url(r'^course/create$', views.create),
]
