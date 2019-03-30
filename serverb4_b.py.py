import socket

class Server():
    def __init__(self):
        self.palabra = ""
        self.palabra_oculta = ""
        self.palabra_oculta_temp = ""
        self.temp_var = ""
        self.num_error = 0
        self.game_over = False
        self.win = False

        self.error = {
        0 : "\t ______\n\t |    |\n\t      |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
        1 : "\t ______\n\t |    |\n\t O    |\n\t      |\n\t      |\n\t      |\n\t______|_\n\n",
        2 : "\t ______\n\t |    |\n\t O    |\n\t |    |\n\t      |\n\t      |\n\t______|_\n\n",
        3 : "\t ______\n\t |    |\n\t O    |\n\t/|    |\n\t      |\n\t      |\n\t______|_\n\n",
        4 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/     |\n\t      |\n\t______|_\n\n",
        5 : "\t ______\n\t |    |\n\t O    |\n\t/|\   |\n\t/ \   |\n\t      |\n\t______|_\n\n",
        6 : "\t Fin"
        }

        self.mi_socket = socket.socket()
        self.mi_socket.bind(("127.0.0.1",9999))
        self.mi_socket.listen(1)
        conexion, direccion = self.mi_socket.accept()

        self.asignar_palabra()

        while True:
            mensaje = conexion.recv(1024)
            print(">>: "+mensaje.decode())

            self.if_game_over()
            if self.game_over == False:
                self.buscar_letra(mensaje.decode())
                conexion.send(self.print_ahorcado().encode()+self.print_palabra_oculta().encode())
            if self.win == True:
                conexion.send("\n     Gano".encode())
            if self.game_over == True and self.win == False:
                conexion.send("\n      Perdio".encode())

        print("Cerrar")

    def print_ahorcado(self):
        return self.error[self.num_error]

    def asignar_palabra(self):
        self.palabra = "programar"
        for letra in range(len(self.palabra)):
            self.palabra_oculta = self.palabra_oculta + "_"

    def print_palabra_oculta(self):
        if self.num_error <= 5:
            self.palabra_oculta_temp = ""

            for letra in range(len(self.palabra)):
                self.palabra_oculta_temp = self.palabra_oculta_temp + self.palabra_oculta[letra] + " "

            return self.palabra_oculta_temp

    def buscar_letra(self, letra):
        if self.num_error <= 5:
            self.temp_var = ""
            for pos in range(len(self.palabra)):
                if self.palabra[pos] == str(letra):
                    self.temp_var = self.temp_var + str(letra)
                else:
                    self.temp_var = self.temp_var + self.palabra_oculta[pos]
            if self.palabra_oculta == self.temp_var and self.num_error < 6:
                self.num_error = self.num_error + 1
            self.palabra_oculta = self.temp_var

    def if_game_over(self):
        if self.num_error >= 5:
            self.game_over = True
        if self.palabra == self.palabra_oculta:
            self.win = True

server = Server()