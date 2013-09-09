from django.conf.urls import patterns, include, url

from .views import ListContacts, ViewContact, DeleteContact, UpdateContact, AddContact


urlpatterns = patterns('',
	url(r'^all/$', ListContacts.as_view(), name='list_contacts'),
	url(r'^add/$', AddContact.as_view(), name='add_contact'),
	url(r'^delete/(?P<pk>\d+)/$', DeleteContact.as_view(), name='delete_contact'),
	url(r'^update/(?P<pk>\d+)/$', UpdateContact.as_view(), name='update_contact'),
	url(r'^view/(?P<pk>\d+)/$', ViewContact.as_view(), name='view_contact'),
)
