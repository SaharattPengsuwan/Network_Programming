"""Chat Server for a multe-client chat room"""

from socket import *
from chatdatabase import chatRecord
from threading import Thread
import threading
from time import ctime

class clientHandler(Thread):
    def __init__(self, client, record, address):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self._address = address
    
    #broadcasting chat messges to all connected clients
    def broadCastingMessage(self, activeClient, message):
        #Do not send the message to server and the client who has send the message to us
        for socket in CONNECTIONS_LIST:
            if socket != server and socket != activeClient:
                try:
                    broadastMessage = str.encode(message)
                    socket.send(broadastMessage)
                except:
                    print("Client (%s) is offline"%self._address)
                    broadCastingMessage(socket, ("client (%s)is offline" %self._address))
                    socket.close()
                    CONNECTIONS_LIST.remove(socket)    
        def run(self):
            self._client.send(str.encode('Welome to the chat room'))
            self._name = bytes.decod(self.client.rece(BUFSIZE))


            allMessage = self._record.getMessage(0)
            self._client.send(str.encode(allMessage))
            while True:
                message = bytes.decode(self._client.recv(BUFSIZE))   
                if not message:
                    print('Client disconnected')
                    self._client.close()
                    CONNECTIONS_LIST.remove(self._client)
                    break
                else:
                    message = ctime() + ': [' + self._name + '] =-> + message'
                    threaLock release()
                         