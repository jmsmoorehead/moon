from django.db import models

import datetime
# Create your models here.

from contact.models import Contact

class Withdrawal(models.Model):
    amount = models.FloatField()
    contact = models.ForeignKey(Contact)
    created = models.DateField(default=datetime.datetime.today)
    
    def __unicode__(self):
        return "%s from %s on %s" % (self.amount, self.contact, self.created)
    
    class Meta:
        ordering = ['-created']
        
class Deposit(models.Model):
    amount = models.FloatField()
    contact = models.ForeignKey(Contact)
    created = models.DateField(default=datetime.datetime.today)

    def __unicode__(self):
        return "%s from %s on %s" % (self.amount, self.contact, self.created)

    class Meta:
        ordering = ['-created']
        