# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shareboards'
        db.create_table(u'sampleapp_shareboards', (
            ('groupid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampleapp.Groups'])),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sampleapp.User'], unique=True, primary_key=True)),
            ('itemname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('ratings', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('decision', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sampleapp', ['Shareboards'])

        # Adding model 'Groups'
        db.create_table(u'sampleapp_groups', (
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sampleapp.User'])),
            ('groupname', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'sampleapp', ['Groups'])


    def backwards(self, orm):
        # Deleting model 'Shareboards'
        db.delete_table(u'sampleapp_shareboards')

        # Deleting model 'Groups'
        db.delete_table(u'sampleapp_groups')


    models = {
        u'sampleapp.groups': {
            'Meta': {'object_name': 'Groups'},
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampleapp.User']"})
        },
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
        u'sampleapp.shareboards': {
            'Meta': {'object_name': 'Shareboards'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'decision': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'groupid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sampleapp.Groups']"}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ratings': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sampleapp.User']", 'unique': 'True', 'primary_key': 'True'})
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