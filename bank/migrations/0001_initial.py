# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Withdrawal'
        db.create_table(u'bank_withdrawal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Contact'])),
        ))
        db.send_create_signal(u'bank', ['Withdrawal'])

        # Adding model 'Deposit'
        db.create_table(u'bank_deposit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Contact'])),
        ))
        db.send_create_signal(u'bank', ['Deposit'])


    def backwards(self, orm):
        # Deleting model 'Withdrawal'
        db.delete_table(u'bank_withdrawal')

        # Deleting model 'Deposit'
        db.delete_table(u'bank_deposit')


    models = {
        u'bank.deposit': {
            'Meta': {'object_name': 'Deposit'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bank.withdrawal': {
            'Meta': {'object_name': 'Withdrawal'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Contact']"}),
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