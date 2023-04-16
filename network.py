import socket
import pickle

class NetWork:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP():
        return self.p
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode())
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)