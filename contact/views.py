# Create your views here.
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from .models import Contact, ContactBook
from .forms import ContactForm, ContactBookForm

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
		return reverse('contactbook_create', kwargs={'contact_id': self.object.pk})


class ContactBookDelete(DeleteView):
    model = ContactBook

    def get_success_url(self):
		return reverse('contact_detail', kwargs={'pk': self.object.contact.pk})

class ContactBookCreate(CreateView):
    model = ContactBook
    form_class = ContactBookForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        contact = get_object_or_404(Contact, pk=self.kwargs['contact_id'])
        self.object.contact = contact
        self.object.save()
        return super(ContactBookCreate, self).form_valid(form)

    def get_success_url(self):
		return reverse('contact_detail', kwargs={'pk': self.object.contact.pk})
