from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^post/create', views.create),
  url(r'^post/save/(?P<post_id>[\w\-]+)/$', views.save),
  url(r'^post/delete', views.delete),
  url(r'^post/edit/(?P<post_id>[\w\-]+)/$', views.edit),
  url(r'^post/show/(?P<post_id>[\w\-]+)/$', views.show),
]
