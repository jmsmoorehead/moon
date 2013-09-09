# Create your views here.
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.core.urlresolvers import reverse


from .models import Book
from .forms import BookForm


class BookList(ListView):
    model = Book
    
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
	
    def get_success_url(self):
		return reverse('book_detail', kwargs={'pk': self.kwargs['pk']})
    
class BookDelete(DeleteView):
    model = Book

    def get_success_url(self):
        return reverse('book_list')
		
class BookDetail(DetailView):
    model = Book
    
class BookCreate(CreateView):
	model = Book
	form_class = BookForm

	def get_success_url(self):
		return reverse('book_list')