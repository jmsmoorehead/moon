from django.db import models


import datetime

# Create your models here.
from book.models import Book


class Contact(models.Model):
    name = models.CharField(blank=True, max_length=100)
    books = models.ManyToManyField(Book, through='ContactBook')
    
    
class ContactBook(models.Model):
    contact = models.ForeignKey(Contact)    
    book = models.ForeignKey(Book)
    date_loaned = models.DateField(default=datetime.datetime.today)
    