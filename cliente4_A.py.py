import threading
import socket
import sys

class Client():
    def ___init___(self, host="localhost", port=9992):
        self.sock = socket.socket()
        self.sock.connect((host, port))

        msj_server = threading.Thread(target=self.msj_ser)
        msj_server.setDaemon = True
        msj_server.start()

        url = input("\nOpciones:\n\n"
                        "1. Webscraping a Neftlix.\n"
                        "2. Salir.\n\n"
                    "Respuesta -> ")

        while True:
            self.enviar_msj(url)
            url = ""

    def msj_ser(self):
        try:
            data = self.sock.recv(1024)
            if data:
                print("Retorno -> ",data.decode())
        except:
            print("Error inesperado")
            self.sock.close()
            sys.exit()

    def enviar_msj(self, url):
        self.sock.send(url.encode())

client = Client()