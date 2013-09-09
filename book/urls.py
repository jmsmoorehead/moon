from django.conf.urls import patterns, include, url

from .views import BookCreate, BookDelete, BookUpdate, BookList, BookDetail


urlpatterns = patterns('',

	url(r'^all/$', BookList.as_view(), name='book_list'),
	url(r'^create/$', BookCreate.as_view(), name='book_create'),
	url(r'^delete/(?P<pk>\d+)/$', BookDelete.as_view(), name='book_delete'),
	url(r'^update/(?P<pk>\d+)/$', BookUpdate.as_view(), name='book_update'),
	url(r'^view/(?P<pk>\d+)/$', BookDetail.as_view(), name='book_detail'),
)
