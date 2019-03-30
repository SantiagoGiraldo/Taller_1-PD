import socket

from dictionary import Data

class Server():
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(("", 9091))
        self.sock.listen(1)
        self.connection, address = self.sock.accept()

        while True:
            self.msj = self.connection.recv(1024)
            print("[]: " + self.msj.decode())

            dictionary = Data()
            self.msj = dictionary.translate(self.msj.decode())

            self.connection.send("[Codigo Binario]: ".encode() + str(self.msj).encode())

        print("closed")
        self.connection.close()
        self.sock.close()

server = Server()