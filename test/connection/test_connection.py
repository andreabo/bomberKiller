__author__ = 'Fredy Garcia, Carol Bohorquez'

import socket
from unittest import TestCase
from pymock.pymock import Controller
from bomberkiller.connection.connection import Connection


class TestConnection(TestCase):

    def __init__(self, method_name=None):
        super(TestConnection, self).__init__(method_name)

    def setUp(self):
        super(TestConnection, self).setUp()
        self.controller = Controller()
        self.connection = Connection()

    def tearDown(self):
        super(TestConnection, self).tearDown()
        pass

    def test_connect(self):
        try:
            self.connection.connect("NoHost", 12345)
            self.fail("Connection should not have been achieved")
        except IOError:
            pass
        finally:
            self.connection.disconnect()

        self.connection.client = self.controller.mock()
        self.controller.expects(self.connection.client.connect(("Something", 12345)))
        self.controller.expectAndReturn(self.connection.client.recv(2048), "Ingrese usuario y token:")
        self.controller.expects(self.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.connection.client.close())
        self.controller.replay()
        try:
            self.connection.connect("Something", 12345)
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.connection.disconnect()

    def test_login(self):
        try:
            self.connection.login("NoUsername", "NoToken")
            self.fail("Login should not have been achieved")
        except IOError:
            pass
        finally:
            self.connection.disconnect()

        self.connection.client = self.controller.mock()
        self.controller.expects(self.connection.client.send("%s,%s" % ("Username", "Token")))
        self.controller.expects(self.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.connection.client.close())
        self.controller.replay()
        try:
            self.connection.login("Username", "Token")
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.connection.disconnect()

    def test_disconnect(self):
        self.connection.connected = False
        self.connection.disconnect()

        self.connection.connected = True
        self.connection.disconnect()

        self.connection.client = self.controller.mock()
        self.controller.expects(self.connection.client.send("%s,%s" % ("Username", "Token")))
        self.controller.expects(self.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.connection.client.close())
        self.controller.replay()

        self.connection.connected = False
        self.connection.disconnect()

        self.connection.connected = True
        self.connection.disconnect()

    def test_read_message(self):
        try:
            message = self.connection.read_message()
            self.fail("Read message should not have been achieved, message: %s " % message)
        except IOError:
            pass
        finally:
            self.connection.disconnect()

        self.connection.client = self.controller.mock()
        self.controller.expectAndReturn(self.connection.client.recv(1024), "Received Message")
        self.controller.expects(self.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.connection.client.close())
        self.controller.replay()
        try:
            message = self.connection.read_message()
            self.assertEqual(message, ["Received Message"])
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.connection.disconnect()

    def test_write_message(self):
        try:
            self.connection.write_message("Test Message")
            self.fail("Write message should not have been achieved")
        except IOError:
            pass
        finally:
            self.connection.disconnect()

        self.connection.client = self.controller.mock()
        self.controller.expects(self.connection.client.send("BE"))
        self.controller.expects(self.connection.client.shutdown(socket.SHUT_RDWR))
        self.controller.expects(self.connection.client.close())
        self.controller.replay()
        try:
            self.connection.write_message("BE")
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.connection.disconnect()
