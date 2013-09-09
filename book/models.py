from django.db import models

# Create your models here.


class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(blank=True, max_length=100)
    
    def __unicode__(self):
        return "%s (ISBN: %s)" % (self.name, self.isbn)