# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Withdrawal'
        db.delete_table(u'bank_withdrawal')

        # Deleting model 'Deposit'
        db.delete_table(u'bank_deposit')

        # Adding model 'Transfer'
        db.create_table(u'bank_transfer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Contact'])),
            ('transfer_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_created', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 14, 0, 0))),
        ))
        db.send_create_signal(u'bank', ['Transfer'])


    def backwards(self, orm):
        # Adding model 'Withdrawal'
        db.create_table(u'bank_withdrawal', (
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('created', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 10, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Contact'])),
        ))
        db.send_create_signal(u'bank', ['Withdrawal'])

        # Adding model 'Deposit'
        db.create_table(u'bank_deposit', (
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('created', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 10, 0, 0))),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.Contact'])),
        ))
        db.send_create_signal(u'bank', ['Deposit'])

        # Deleting model 'Transfer'
        db.delete_table(u'bank_transfer')


    models = {
        u'bank.transfer': {
            'Meta': {'ordering': "['-date_created']", 'object_name': 'Transfer'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.Contact']"}),
            'date_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 9, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transfer_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
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