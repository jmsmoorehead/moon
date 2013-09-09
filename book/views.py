# Create your views here.
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.core.urlresolvers import reverse


from .models import Book
from .forms import CreateBookForm


class ListBooks(ListView):
    model = Book
    
class UpdateBook(UpdateView):
    model = Book
    form_class = CreateBookForm
	
    def get_success_url(self):
		return reverse('book_detail', kwargs={'pk': self.kwargs['pk']})
    
class DeleteBook(DeleteView):
    model = Book

    def get_success_url(self):
        return reverse('list_books')
		
class DetailBook(DetailView):
    model = Book
    
class CreateBook(CreateView):
	model = Book
	form_class = CreateBookForm

	def get_success_url(self):
		return reverse('list_books')