from django.conf.urls import patterns, include, url

from .views import (
    ContactList, ContactDetail, ContactDelete, ContactUpdate, ContactCreate,
    ContactBookCreate, ContactBookDelete
)

urlpatterns = patterns('',
	url(r'^all/$', ContactList.as_view(), name='contact_list'),
	url(r'^add/$', ContactCreate.as_view(), name='contact_create'),
	url(r'^delete/(?P<pk>\d+)/$', ContactDelete.as_view(), name='contact_delete'),
	url(r'^update/(?P<pk>\d+)/$', ContactUpdate.as_view(), name='contact_update'),
	url(r'^view/(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
	url(r'^add-book/(?P<contact_id>\d+)/$', ContactBookCreate.as_view(), name='contactbook_create'),
	url(r'^delete-book/(?P<pk>\d+)/$', ContactBookDelete.as_view(), name='contactbook_delete'),


)
