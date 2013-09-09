from django import forms

from .models import Contact, ContactBook

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', )

class ContactBookForm(forms.ModelForm):
    
    class Meta:
        model = ContactBook
        fields = ('book',)
        