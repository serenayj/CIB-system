import os

from twisted.application import service, internet
from twisted.internet import reactor

from twisted.web import wsgi
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.websockets import WebSocketsResource, lookupProtocolForFactory

from twisted_share.factories import ShareFactory
from twisted_share.resources import HttpShare, StaticFileScanner
from twisted_share.wsgi import WsgiRoot
from twisted.python.threadpool import ThreadPool

from django.core.handlers.wsgi import WSGIHandler



shared_messages = {}

resource = HttpShare(shared_messages)
factory = Site(resource)
ws_resource = WebSocketsResource(lookupProtocolForFactory(resource.wsFactory))

root = Resource()
root.putChild("",resource) #the http protocol is up at /
root.putChild("ws",ws_resource) #the websocket protocol is at /ws

application = service.Application("shareserver")
internet.TCPServer(1035, Site(root)).setServiceParent(application)

#serving django over wsgi
# Create and start a thread pool,
wsgiThreadPool = ThreadPool()
wsgiThreadPool.start()

django_application = WSGIHandler()
django_resource = wsgi.WSGIResource(reactor, wsgiThreadPool, django_application)

django_root = WsgiRoot(django_resource)
project_dir = os.getcwd()
django_root.putChild('static', StaticFileScanner(project_dir + "/cib_simulator/static"))

internet.TCPServer(8000, Site(django_root)).setServiceParent(application)
