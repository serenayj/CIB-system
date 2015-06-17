from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class ChatHistory(models.Model):
	username = models.ForeignKey(User)
	chatroomid = models.ForeignKey(ChatRoom)
	text = models.CharField(max_length=255)

	def _unicode_(self):
		return self.name

class CommHistory(models.Model):
	username = models.ForeignKey(User)
	record = models.TextField()
	record_type = models.CharField(max_length=10)
	#time?


class ShareHistory(models.Model):
	username = models.ForeignKey(User)
	record_name= models.TextField()
	record_url = models.TextField()
	record_type = models.CharField(max_length=10)
		
