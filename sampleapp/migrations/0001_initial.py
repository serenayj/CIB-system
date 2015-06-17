# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'sampleapp_user', (
            ('userid', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'sampleapp', ['User'])

        # Adding model 'Items'
        db.create_table(u'sampleapp_items', (
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampleapp.User'])),
            ('itemsid', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('itemname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('ratings', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('decision', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sampleapp', ['Items'])

        # Adding model 'Queryhistory'
        db.create_table(u'sampleapp_queryhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampleapp.User'])),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'sampleapp', ['Queryhistory'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'sampleapp_user')

        # Deleting model 'Items'
        db.delete_table(u'sampleapp_items')

        # Deleting model 'Queryhistory'
        db.delete_table(u'sampleapp_queryhistory')


    models = {
        u'sampleapp.items': {
            'Meta': {'object_name': 'Items'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'decision': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'itemsid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'ratings': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampleapp.User']"})
        },
        u'sampleapp.queryhistory': {
            'Meta': {'object_name': 'Queryhistory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampleapp.User']"})
        },
        u'sampleapp.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['sampleapp']