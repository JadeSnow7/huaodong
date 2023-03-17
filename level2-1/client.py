import random
import socket


methods=['OPTIONS', 'SETUP', 'PLAY', 'TEARDOWN']
class request:
    client = socket.socket()
    ip = socket.gethostbyname(socket.gethostname())
    #msg = ''
    CSeq = 1

    def __init__(self, host=socket.gethostname(), port=1230):

        self.host=host
        self.port=port
        self.url = f'diantp://{host}:{port}'
        self.vertion = 0.5
        self.client.connect((host,port))


    def message(self) -> str:
        for i in methods:
            self.msg = f'{i} {self.url} {self.vertion}\r\nCSeq:{self.CSeq}\r\n'
            self.xxx(i)
            self.CSeq+=1
            print(f'{self.msg}\r\n')
        return self.msg

    def xxx(self,i):
        if i=='OPTIONS':
            msg=self.msg
        elif i=='SETUP':
            msg=f'{self.msg}Transport:TCP\r\nclient_port={self.port}\r\n'

        elif i=='PLAY':

            self.id = self.client.recv(1024).decode('utf-8')
            msg=f'{self.msg}Session_id={self.id}\r\nRange:ntp:{0}-{15}\r\n'


        elif i=='TURNDOWN':

            msg=f'{self.msg}Session_id={self.id}\r\n'
        else:
            msg='WARNING:Wrong message'
        print(msg)
        self.client.send(msg.encode('utf-8'))
    def __del__(self):
        self.client.close()
        print('\n断开连接\n')
x=request()
#while True:
msg=x.message()
