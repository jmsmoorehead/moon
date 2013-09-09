# Create your views here.
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)


from .models import Contact


class ListContacts(ListView):
    pass

class ViewContact(DetailView):
    pass
    
class DeleteContact(CreateView):
    pass

class UpdateContact(CreateView):
    pass

class AddContact(CreateView):
    pass

    