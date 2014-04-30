__author__ = 'Fredy Garcia, Carol Bohorquez'

from bomberkiller.game.strategy import Strategy
from bomberkiller.game.action import Action
from datetime import datetime


class Game:

    def __init__(self):
        self.strategy = None

    # Prepare
    def prepare(self):
        self.print_prepare_message()

    # Start
    def start(self, player_character, map_):
        self.strategy = Strategy(player_character)
        self.strategy.create_board(map_)
        self.strategy.locate_elements()
        self.strategy.calculate_bomb_ranges()
        self.print_start_message(self.strategy.player_character, self.strategy.board)

    # Turn
    def turn(self, turn_number, map_):
        self.strategy.create_board(map_)
        self.strategy.locate_elements()
        self.strategy.update_rules_information()
        self.strategy.calculate_bomb_ranges()
        self.print_turn_message(self.strategy.board, self.strategy.player_character, turn_number)
        self.strategy.calculate_effort()
        self.strategy.calculate_action()
        self.print_action(self.strategy.player_character, self.strategy.action)
        return self.strategy.action

    # Lost
    def lost(self):
        self.print_lost_message(self.strategy.player_character)
        self.strategy = None

    # Already connected
    def already_connected(self):
        self.print_already_connected_message()
        self.strategy = None

    # Wrong messages
    def wrong_messages(self, wrong_messages_number):
        self.print_wrong_messages_message(wrong_messages_number)
        self.strategy = None

    # End
    def end(self):
        self.print_end_message()
        self.strategy = None

    @staticmethod
    def print_prepare_message():
        print "*******************************************************************************"
        print "Esperando a que otros jugadores se conecten"

    @staticmethod
    def print_start_message(character, board):
        print "*******************************************************************************"
        print "*******************************************************************************"
        print "-------------------------------------------------------------------------------"
        print "Iniciando una nueva partida. Nuestro robot es %s" % character
        print "Mapa inicial:"
        print board
        print "-------------------------------------------------------------------------------"

    @staticmethod
    def print_turn_message(board, player_character, turn_number):
        print "-------------------------------------------------------------------------------"
        print "Turno numero: %s. Robot: %s. Fecha y hora: %s" % (turn_number, player_character, datetime.now())
        print "Mapa actual:"
        print board

    @staticmethod
    def print_action(character, action):
        if action == Action.EAST:
            print "(Comando: %s) Nuestro robot %s se va a mover al Este" % (action, character)
        if action == Action.WEST:
            print "(Comando: %s) Nuestro robot %s se va a mover al Oeste" % (action, character)
        if action == Action.NORTH:
            print "(Comando: %s) Nuestro robot %s se va a mover al Norte" % (action, character)
        if action == Action.SOUTH:
            print "(Comando: %s) Nuestro robot %s se va a mover al Sur" % (action, character)
        if action == Action.BOMB_EAST:
            print "(Comando: %s) Nuestro robot %s va a colocar una bomba al Este ************** >" % (action, character)
        if action == Action.BOMB_WEST:
            print "(Comando: %s) Nuestro robot %s va a colocar una bomba al Oeste ************* <" % (action, character)
        if action == Action.BOMB_NORTH:
            print "(Comando: %s) Nuestro robot %s va a colocar una bomba al Norte ************* ^" % (action, character)
        if action == Action.BOMB_SOUTH:
            print "(Comando: %s) Nuestro robot %s va a colocar una bomba al Sur *************** v" % (action, character)
        if action == Action.PASS:
            print "(Comando: %s) Nuestro robot %s se va a quedar quieto [ZZZZzzzzZZZzzzZZzzZzZzZ]" % (action, character)

    @staticmethod
    def print_already_connected_message():
        print "Ya nos encontramos conectados al servidor desde un lugar diferente "

    @staticmethod
    def print_wrong_messages_message(wrong_messages_number):
        print 'Se han recibido %s mensajes erroneos. Deteniendo juego.' % wrong_messages_number

    @staticmethod
    def print_lost_message(character):
        print "-------------------------------------------------------------------------------"
        print "Nuestro robot %s ha sido cruelmente asesinado. :(" % character
        print "-------------------------------------------------------------------------------"

    @staticmethod
    def print_end_message():
        print "-------------------------------------------------------------------------------"
        print "********************************* Hasta Luego *********************************"
        print "-------------------------------------------------------------------------------"
        print "******************************** Fin del Juego ********************************"
        print "*******************************************************************************"