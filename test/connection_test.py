__author__ = 'Fredy Garcia, Carol Bohorquez'

import unittest
from bomberkiller.connection import Connection


class ConnectionTest(unittest.TestCase):

    def setUp(self):
        self.connection = Connection()

    def test_connect(self):
        try:
            self.connection.connect("NoHost", 12345)
            self.fail("Connection should not have been achieved")
        except IOError:
            pass
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

    def test_disconnect(self):
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

    def test_write_message(self):
        try:
            self.connection.write_message("Test Message")
            self.fail("Write message should not have been achieved")
        except IOError:
            pass
        finally:
            self.connection.disconnect()
