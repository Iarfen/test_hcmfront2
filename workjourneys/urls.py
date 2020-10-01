from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<workjourney_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^create/send/$', views.create_send, name='create_send'),
    url(r'^(?P<workjourney_id>[0-9]+)/delete$', views.delete, name='delete'),
    url(r'^(?P<workjourney_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<workjourney_id>[0-9]+)/edit/send/$', views.edit_send, name='edit_send'),
]
