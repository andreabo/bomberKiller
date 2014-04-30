__author__ = 'Fredy Garcia, Carol Bohorquez'

import socket
from unittest import TestCase
from pymock.pymock import Controller
from bomberkiller.killer import BomberKiller
from bomberkiller.game.turn import Turn
from bomberkiller.game.action import Action


class TestKiller(TestCase):
    def __init__(self, method_name=None):
        super(TestKiller, self).__init__(method_name)

    def setUp(self):
        super(TestKiller, self).setUp()
        self.controller = Controller()
        self.killer = BomberKiller("Something", 12345, "Username", "Token")

    def tearDown(self):
        super(TestKiller, self).tearDown()

    def test_killer(self):
        pass

    def test_run(self):
        self.killer.connection.client = self.controller.mock()
        self.killer.playing = True
        self.controller.expects(self.killer.connection.client.connect(("Something", 12345)))
        self.controller.expectAndReturn(self.killer.connection.client.recv(2048), "Ingrese usuario y token:")
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), "Usuario ya esta conectado")
        self.controller.expects(self.killer.connection.client.send("%s,%s" % ("Username", "Token")))
        self.controller.expects(self.killer.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.killer.connection.client.close())
        self.controller.replay()

        self.killer.run()

        self.controller.reset()
        self.killer.connection.client = self.controller.mock()
        self.killer.playing = True
        self.controller.expects(self.killer.connection.client.connect(("Something", 12345)))
        self.controller.expectAndReturn(self.killer.connection.client.recv(2048), "Ingrese usuario y token:")
        self.controller.expectAndRaise(self.killer.connection.client.recv(1024), KeyboardInterrupt("Stopping App"))
        self.controller.expects(self.killer.connection.client.send("%s,%s" % ("Username", "Token")))
        self.controller.expects(self.killer.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.killer.connection.client.close())
        self.controller.replay()

        self.killer.run()

        self.controller.reset()
        self.killer.connection.client = self.controller.mock()
        self.killer.playing = True
        self.controller.expects(self.killer.connection.client.connect(("Something", 12345)))
        self.controller.expectAndReturn(self.killer.connection.client.recv(2048), "Ingrese usuario y token:")
        self.controller.expectAndRaise(self.killer.connection.client.recv(1024), IOError("IO Error"))
        self.controller.expects(self.killer.connection.client.send("%s,%s" % ("Username", "Token")))
        self.controller.expects(self.killer.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.killer.connection.client.close())
        self.controller.expects(self.killer.connection.client.connect(("Something", 12345)))
        self.controller.expectAndReturn(self.killer.connection.client.recv(2048), "Ingrese usuario y token:")
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), "Usuario ya esta conectado")
        self.controller.expects(self.killer.connection.client.send("%s,%s" % ("Username", "Token")))
        self.controller.expects(self.killer.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.killer.connection.client.close())
        self.controller.replay()

        self.killer.run()

    def test_play(self):
        self.killer.connection.client = self.controller.mock()
        self.killer.max_wrong_messages_number = 3
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), Turn.START + ";"
                                                                                               "X,X,X,X,X,X,X,X,X,X,X\n"
                                                                                               "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                               "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                               "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                               "X,_,_,_,P,2,B,_,_,_,X\n"
                                                                                               "X,_,_,_,2,A,2,_,_,_,X\n"
                                                                                               "X,_,_,_,D,2,C,_,_,_,X\n"
                                                                                               "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                               "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                               "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                               "X,X,X,X,X,X,X,X,X,X,X"
                                                                                               ";A")
        self.controller.expects(self.killer.connection.client.send(Action.PASS))
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), Turn.TURN + ";1;"
                                                                                              "X,X,X,X,X,X,X,X,X,X,X\n"
                                                                                              "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                              "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                              "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                              "X,_,_,_,P,1,B,_,_,_,X\n"
                                                                                              "X,_,_,_,1,A,1,_,_,_,X\n"
                                                                                              "X,_,_,_,D,1,C,_,_,_,X\n"
                                                                                              "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                              "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                              "X,_,_,_,_,_,_,_,_,_,X\n"
                                                                                              "X,X,X,X,X,X,X,X,X,X,X")
        self.controller.expects(self.killer.connection.client.send(Action.PASS))
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), Turn.LOST)
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), "Wrong Messages")
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), "Wrong Messages")
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), "Wrong Messages")
        self.controller.expectAndReturn(self.killer.connection.client.recv(1024), "Wrong Messages")
        self.controller.replay()

        self.killer.play()