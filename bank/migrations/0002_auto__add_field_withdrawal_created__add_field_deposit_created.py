# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Withdrawal.created'
        db.add_column(u'bank_withdrawal', 'created',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Deposit.created'
        db.add_column(u'bank_deposit', 'created',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 10, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Withdrawal.created'
        db.delete_column(u'bank_withdrawal', 'created')

        # Deleting field 'Deposit.created'
        db.delete_column(u'bank_deposit', 'created')


    models = {
        u'bank.deposit': {
            'Meta': {'object_name': 'Deposit'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Contact']"}),
            'created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 9, 10, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bank.withdrawal': {
            'Meta': {'object_name': 'Withdrawal'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Contact']"}),
            'created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 9, 10, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['bank']