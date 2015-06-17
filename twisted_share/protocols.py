import time
from twisted.protocols import basic
from twisted.enterprise import adbapi
from twisted_share.dbpool import dbpool
from twisted.internet import reactor
import json 

#dbpool = adbapi.ConnectionPool("sqlite3", "test.sqlite")
    
class WebsocketShare(basic.LineReceiver):

    def connectionMade(self):
        print "Got new client!"
        self.transport.write('connected ....\n')
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "Lost a client!"
        self.factory.clients.remove(self)

    #receive data and save to database    
    def dataReceived(self, data):
        print "got data which is: ",data
        temp = eval(data)
        #print temp['text']
        self.factory.messages[float(time.time())] = data
        self.updateClients(data)

        with open('chat.json','w') as f:
            json.dump(data,f)

    def updateClients(self, data):
        for c in self.factory.clients:
            c.message(data)

    def message(self, message):
        print "got a message which is: ",message
        self.transport.write(message + '\n')





