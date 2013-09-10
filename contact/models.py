from django.db import models



# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    phone = models.CharField(blank=True, max_length=100)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
