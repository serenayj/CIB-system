from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth import models
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

import os
import json,re

from chat.models import *


@csrf_exempt
def saverecord(request):

	history = request.REQUEST.get('history', 'nohistory')
	savehistory = eval(history)
	print savehistory
	thisuser = User.objects.get(username=savehistory['userid'])
	# if elif etc
	try:
		if savehistory['type'] == "chat":
			historytosave = CommHistory(username = thisuser, record = savehistory['text'], record_type = savehistory['type'])
		else:
			historytosave = CommHistory(username = thisuser, record = savehistory['name'], record_type = savehistory['type'])

	except Exception as e:
		print 
		print '%s (%s)' % (e.message, type(e))
	
	historytosave.save()
	
	return HttpResponse('', content_type='application/json')



@login_required
def chat_room(request, chat_room_id):
    chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    return render(request, 'chats/chat_room.html', {'chat': chat})

#@login_required
#def longpoll_chat_room(request, chat_room_id):
    #chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    #return render(request, 'chats/longpoll_chat_room.html', {'chat': chat})

