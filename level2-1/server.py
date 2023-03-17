import random
import socket
import re
class request:
    server=socket.socket()
    ip=socket.gethostbyname(socket.gethostname())
    clients=[]
    def __init__(self,host=socket.gethostname(),port=1230):
        self.server.bind((host,port))
        self.server.listen(5)
        self.client,self.addr=self.server.accept()
        #self.msg=client.recv(1024)

        #print(self.msg)
    def response(self):

        #msg=self.msg.decode('utf-8')
        for i in range(4):
            msg=self.client.recv(1024).decode('utf-8')

            if 'OPTIONS' in msg:
                print('Success')
            elif 'SETUP' in msg:
                id = random.randint(0, 1000)
                self.client.send(f'{id}'.encode('utf-8'))
                self.clients.append((self.client,id))
                pass
            elif 'PLAY' in msg:

                pass
            elif 'TEARDOWN' in msg:
                pass
            else:
            #print('WARNING:Wrong information')
                pass
    def __del__(self):
        self.server.close()
x=request()
print("连接地址：%s"%str(x.addr))
while True:
    x.response()
    pass


