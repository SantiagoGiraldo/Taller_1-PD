import socket
import string
import time

class Client():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('127.0.0.1',9999))

        print("Ahorcado")
        time.sleep(1)
        print("\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n")

        while True:
            mensaje = input(">> ")
            self.mi_socket.send(mensaje.encode())
            if(mensaje == 'cerrar'):
                break

            print("Ahorcado")
            recibido = self.mi_socket.recv(1024)
            print(recibido.decode())

        print("GoodBye")
        self.mi_socket.close()

client = Client()
