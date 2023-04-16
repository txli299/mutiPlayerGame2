import socket
from _thread import *
from game import Game
import pickle

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,255,0))]

def threaded_client(conn,p, gameId):
    pass


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client,(conn))
