import socket
import string
import time


class Client():
    def __init__(self):
        self.mi_socket = socket.socket()
        self.mi_socket.connect(('localhost',9999))

        global nombre
        nombre = input("Ingrese su nombre: >> ")
        self.mi_socket.send(nombre.encode())
        recibido = self.mi_socket.recv(1024)
        print(recibido.decode())
        time.sleep(.300)

        while True:
            mensaje = input(nombre+">> ")
            self.mi_socket.send(mensaje.encode())
            if mensaje == 'cerrar sesion':
                break
            recibido = self.mi_socket.recv(1024)
            print(recibido.decode())

        print("Hasta luego,regresa pronto")
        self.mi_socket.close()

client = Client()