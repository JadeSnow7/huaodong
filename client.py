import socket
methods=['OPTIONS', 'SETUP', 'PLAY', 'TEARDOWN']
class TcpClient:
    def __init__(self, host=socket.gethostname(), port=8888):
        self.host=host
        self.port=port
        self.url = f'diantp://{host}:{port}'
        self.vertion = 0.5
        self.CSeq=1
        self.client=socket.socket()
        self.client.connect((host,port))
        self.session_record=[]
        self.id=0
    def message(self) -> str:
        for i in methods:
            self.msg = f'{i} {self.url} version={self.vertion}\r\nCSeq:{self.CSeq}\r\n'
            self.xxx(i)
            self.CSeq+=1
    def xxx(self,i):
        if i=='OPTIONS':
            msg=self.msg
        elif i=='SETUP':
            msg=f'{self.msg}Transport:TCP\r\nclient_port={self.port}\r\n'
        elif i=='PLAY':
            self.id = self.client.recv(1024).decode('utf-8')
            print(self.id)
            message=self.client.recv(1024).decode('utf-8')
            msg=f'{self.msg}Session_id={self.id}\r\nRange:ntp:{0}-{15}\r\n'
            print(message)
        elif i=='TEARDOWN':
            msg=f'{self.msg}Session_id={self.id}\r\n'
        else:
            msg='WARNING:Wrong message'
        self.client.send(msg.encode('utf-8'))
        self.session_record.append(f'{msg}\r\n')
        print(msg)
    def __del__(self):
        self.client.close()
        print(self.session_record)
        print('\n断开连接\n')
x=TcpClient()
x.message()
