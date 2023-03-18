import random
import socket
from threading import Thread
request_record={}
class NewClients():
    def __init__(self):
        self.server=TcpServer()
        self.ID = self.server.response()






class TcpServer:
    def __init__(self, host=socket.gethostname(), port=8888):
        self.server = socket.socket()
        self.ip = socket.gethostbyname(socket.gethostname())

        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind((host, port))
        self.server.listen(5)




    def response(self):
        ID = random.randint(0, 1000)
        client, addr = self.server.accept()
        for i in range(4):
            msg = client.recv(1024).decode('utf-8')
            if 'OPTIONS' in msg:
                print('Success')
            elif 'SETUP' in msg:
                client.send(f'{ID}'.encode('utf-8'))
                print('Success')
            elif 'PLAY' in msg:
                message = ''

                for i in range(5):
                    message += '剑阁峥嵘而崔巍，一夫当关，万夫莫开。\r\n'
                client.send(message.encode('utf-8'))

            elif 'TEARDOWN' in msg:
                self.TcpClients[ID].close()
            else:
                pass
        return ID


s = TcpServer()

s.response()
