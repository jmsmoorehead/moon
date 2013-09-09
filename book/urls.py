from django.conf.urls import patterns, include, url

from .views import CreateBook, DeleteBook, UpdateBook, ListBooks, DetailBook


urlpatterns = patterns('',

	url(r'^all/$', ListBooks.as_view(), name='list_books'),
	url(r'^create/$', CreateBook.as_view(), name='book_create'),
	url(r'^delete/(?P<pk>\d+)/$', DeleteBook.as_view(), name='book_delete'),
	url(r'^update/(?P<pk>\d+)/$', UpdateBook.as_view(), name='book_update'),
	url(r'^view/(?P<pk>\d+)/$', DetailBook.as_view(), name='book_detail'),
)
