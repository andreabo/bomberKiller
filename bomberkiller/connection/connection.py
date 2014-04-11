__author__ = 'Fredy Garcia, Carol Bohorquez'

import socket


class Connection:

    DIVIDER = ";"

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        self.connected = False

    def connect(self, host, port):
        print "Conectando al servidor %s en el puerto %s ..." % (host, port)
        self.client.connect((host, port))
        self.connected = True
        print "Conectado"

        # Reads until user and token request
        message = ""
        while message.find('Ingrese usuario y token:') == -1:
            message = message + self.client.recv(2048)

        # Prints server welcome message
        print message

    def login(self, username, token):
        print "Usuario: %s, Token: %s" % (username, token)

        #Sends username and password to server
        self.client.send("%s,%s" % (username, token))

    def disconnect(self):
        try:
            if self.connected:
                print "Desconectando del servidor..."
                self.client.shutdown(socket.SHUT_RDWR)
                self.client.close()
                print "Desconectado"
            else:
                print "No esta conectado al servidor"
        except IOError as e:
            print "Error desconectando del servidor: %s " % e

    def read_message(self):
        # Reads message from server
        return self.client.recv(1024).split(";")

    def write_message(self, action):
        # Writes message to server
        self.client.send(action)
