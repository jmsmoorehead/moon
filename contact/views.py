# Create your views here.
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.core.urlresolvers import reverse

from .models import Contact
from .forms import ContactForm

class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact
    
class ContactDelete(DeleteView):
    model = Contact
    
    def get_success_url(self):
        return reverse('contact_list')

class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
		return reverse('contact_detail', kwargs={'pk': self.kwargs['pk']})
		
class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
        
    def get_success_url(self):
		return reverse('contact_list')


