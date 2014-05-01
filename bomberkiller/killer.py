__author__ = 'Fredy Garcia, Carol Bohorquez'

from bomberkiller.connection.connection import Connection
from bomberkiller.game.game import Game
from bomberkiller.game.turn import Turn


class Killer(object):

    MAX_WRONG_MESSAGES_NUMBER = 500

    def __init__(self, host, port, username, token):
        self.max_wrong_messages_number = self.MAX_WRONG_MESSAGES_NUMBER
        self.host = host
        self.port = port
        self.username = username
        self.token = token
        self.connection = Connection()
        self.game = Game()
        self.playing = True
        self.executing = True

    def run(self):
        while self.playing:
            try:
                self.connection.connect(self.host, self.port)
                self.connection.login(self.username, self.token)
                self.play()
            except KeyboardInterrupt:
                self.playing = False
                self.executing = False
            except IOError as e:
                print e
                self.playing = True
            finally:
                self.connection.disconnect()
        self.game.end()

    def play(self):
        self.game.prepare()
        wrong_messages_number = 0

        while self.playing:
            message = self.connection.read_message()
            print message

            if message[0] == Turn.START:
                map_ = message[1]
                player_character = message[2].strip()
                self.game.start(player_character, map_)
                action = self.game.turn("0", map_)
                self.connection.write_message(action)

                wrong_messages_number = 0

            elif message[0] == Turn.LOST:
                self.game.lost()

                wrong_messages_number = 0

            elif message[0] == Turn.TURN:
                turn_number = message[1]
                map_ = message[2]
                action = self.game.turn(turn_number, map_)
                self.connection.write_message(action)

                wrong_messages_number = 0

            elif message[0].find(Turn.ALREADY_CONNECTED) >= 0:
                self.game.already_connected()
                self.playing = False

            else:
                wrong_messages_number += 1
                if wrong_messages_number > self.max_wrong_messages_number:
                    self.game.wrong_messages(wrong_messages_number)
                    self.playing = False
