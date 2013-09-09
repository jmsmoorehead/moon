from django.db import models


from core.fields import ISBNField
# Create your models here.


class Book(models.Model):
    isbn = ISBNField(unique=True)
    name = models.CharField(blank=True, max_length=100)