import requests
import bs4
import lxml
import socket
import sys

class Server():
    def ___init___(self, host="localhost", port=9992):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(1)

        print("Iniciando Conexion")
        conexion, direccion = self.sock.accept()

        msj = conexion.recv(1024)

        while True:
            if msj.decode() == '1':
                resp = self.web('http://www.netflix.com')
                conexion.send(resp.encode())
            else:
                print("Hasta Luego")
                self.sock.close()
                sys.exit()

    def web(self, url):
        try:
            array = []
            res = requests.get(url)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            for i in soup.select('.titulo-seccion'):
                array.append(i.text)
        except:
            print("Error inesperado")
            self.sock.close()

        return str(array)

server = Server()

