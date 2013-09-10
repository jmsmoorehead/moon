# Create your views here.
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.core.urlresolvers import reverse

from braces.views import FormValidMessageMixin

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

class ContactUpdate(FormValidMessageMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact/contact_update.html"
    form_valid_message = 'Contact updated!'
    
    
        
    def get_success_url(self):
		return reverse('contact_update', kwargs={'pk': self.kwargs['pk']})
		
class ContactCreate(FormValidMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact/contact_create.html"
    form_valid_message = 'Contact created!'

    def get_success_url(self):
		return reverse('contact_list')


