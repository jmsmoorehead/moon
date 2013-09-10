from django.conf.urls import patterns, include, url

from .views import (
    ContactList, ContactDetail, ContactDelete, ContactUpdate, ContactCreate,
)

urlpatterns = patterns('',
	url(r'^all/$', ContactList.as_view(), name='contact_list'),
	url(r'^add/$', ContactCreate.as_view(), name='contact_create'),
	url(r'^delete/(?P<pk>\d+)/$', ContactDelete.as_view(), name='contact_delete'),
	url(r'^update/(?P<pk>\d+)/$', ContactUpdate.as_view(), name='contact_update'),
	url(r'^view/(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),


)
