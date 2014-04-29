__author__ = 'Fredy Garcia, Carol Bohorquez'

from bomberkiller.connection.connection import Connection
from pymock.pymock import PyMockTestCase


class ConnectionTest(PyMockTestCase):

    def setUp(self):
        super(ConnectionTest, self).setUp()
        self.true_connection = Connection()
        self.fake_connection = self.mock()
        self.fake_connection.connect("Something", 12345)
        self.fake_connection.login("Username", "Token")
        self.fake_connection.disconnect()
        self.expectAndReturn(self.fake_connection.read_message(), "Ingrese usuario y token:")
        self.fake_connection.write_message("Test Message")
        self.replay()

    def tearDown(self):
        super(ConnectionTest, self).tearDown()

    def test_connect(self):
        try:
            self.true_connection.connect("NoHost", 12345)
            self.fail("Connection should not have been achieved")
        except IOError:
            pass
        finally:
            self.true_connection.disconnect()

        try:
            self.fake_connection.connect("Something", 12345)
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            pass

    def test_login(self):
        try:
            self.true_connection.login("NoUsername", "NoToken")
            self.fail("Login should not have been achieved")
        except IOError:
            pass
        finally:
            self.true_connection.disconnect()

        try:
            self.fake_connection.login("Username", "Token")
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.fake_connection.disconnect()

    def test_disconnect(self):
        self.true_connection.connected = False
        self.true_connection.disconnect()

        self.true_connection.connected = True
        self.true_connection.disconnect()

    def test_read_message(self):
        try:
            message = self.true_connection.read_message()
            self.fail("Read message should not have been achieved, message: %s " % message)
        except IOError:
            pass
        finally:
            self.true_connection.disconnect()

        try:
            message = self.fake_connection.read_message()
            self.assertEqual(message, "Ingrese usuario y token:")
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.fake_connection.disconnect()

    def test_write_message(self):
        try:
            self.true_connection.write_message("Test Message")
            self.fail("Write message should not have been achieved")
        except IOError:
            pass
        finally:
            self.true_connection.disconnect()

        try:
            self.fake_connection.write_message("Test Message")
        except IOError as e:
            self.fail("IOError: " % e)
        finally:
            self.fake_connection.disconnect()
