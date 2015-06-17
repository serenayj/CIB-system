# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth import login
from django.contrib.auth.signals import user_logged_in

# Create your models here.
# users and items are for single 

class User(models.Model):
	userid = models.CharField(max_length=30,primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.emailField

	#it is for printing out with normal words
	def _unicode_(self):
		return self.name


class Items(models.Model):
	userid=models.ForeignKey(User)
	itemsid=models.CharField(max_length=30,primary_key=True)
	itemname= models.CharField(max_length=100)
	comments = models.CharField(max_length=254)
	ratings = models.CharField(max_length=30)
	decision=models.BooleanField(deault=False)

	def _unicode_(self):
		return self.name

#Groups and boards contained user and items


class Groups(models.Model):
	user = models.OneToOneField(User,primary_key=True)
	groupid = models.CharField(max_length=30,primary_key=Ture)

	def _unicode_(self):
		return self.name

class Shareboards(models.Model):
	groupid = models.ForeignKey(Groups)
	user = models.OneToOneField(User,primary_key=True)
	itemname= models.CharField(max_length=100)
	comments = models.CharField(max_length=254)
	ratings = models.CharField(max_length=30)
	decision=models.BooleanField(deault=False)

	def _unicode_(self):
		return self.name

class Queryhistory(models.Model):
	userid = models.ForeignKey(User)
	query = models.CharField(max_length=254)

	def _unicode_(self):
		return self.names

class fashion(models.Model):
	name = models.CharField(max_length=30,primary_key=True)
	description=models.CharField(max_length=30)
	price=models.CharField(max_length=30)
	imageurl=models.CharField(max_length=30)

	def _unicode_(self):
		return self.names