from django.db import models

import datetime
# Create your models here.

from contact.models import Contact

TRANSFER_CHOICES = (
    ('W', 'Withdrawal'),
    ('D', 'Deposit'),
)

class WithdrawalManager(models.Manager):
    def get_query_set(self):
        return super(WithdrawalManager, self).get_query_set().filter(transfer_type='W')

class DepositManager(models.Manager):
    def get_query_set(self):
        return super(DepositManager, self).get_query_set().filter(transfer_type='D')


class Transfer(models.Model):
    amount = models.FloatField()
    contact  = models.ForeignKey(Contact)
    transfer_type = models.CharField(max_length=2, choices=TRANSFER_CHOICES)
    date_created = models.DateField(default=datetime.datetime.today)
    objects = models.Manager()
    deposits = DepositManager()
    withdrawals = WithdrawalManager()
    
    def __unicode__(self):
        return "%s: %s" % (self.contact, self.amount)
        
    class Meta:
        ordering = ['-date_created']
