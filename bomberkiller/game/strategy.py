__author__ = 'Fredy Garcia, Carol Bohorquez'

from bomberkiller.elements.element import Element
from bomberkiller.game.action import Action
from bomberkiller.elements.board import Board
from bomberkiller.game.rules import Rules
from random import Random


class Strategy(object):

    def __init__(self, player_character):
        self.player_character = player_character
        self.rules = Rules()
        self.old_board = None
        self.previous_board = None
        self.board = None
        self.action = None
        self.random = Random()

    # Compares two elements determining the move effort value
    @staticmethod
    def move_effort_comparator(a, b):
        return cmp(a.move_effort, b.move_effort)

    # Create the board according to received map
    def create_board(self, map_):
        if self.previous_board is None:
            self.old_board = Board()
        else:
            self.old_board = self.previous_board
        if self.board is None:
            self.previous_board = Board()
        else:
            self.previous_board = self.board
        self.board = Board()
        for y, line in enumerate(map_.split('\n')):
            row_elements = []
            for x, cell_type in enumerate(line.split(",")):
                element = Element(cell_type.strip(), x, y)
                row_elements.append(element)
            self.board.elements.append(row_elements)

    # Locate all important elements in board
    def locate_elements(self):
        for row_elements in self.board.elements:
            for element in row_elements:
                if element.is_alive_player():
                    if element.type == self.player_character:
                        self.board.bomber_killer = element
                    else:
                        self.board.enemies.append(element)
                elif element.is_power():
                    self.board.powers.append(element)
                elif element.is_bomb():
                    self.board.bombs.append(element)

    # Update rules information
    def update_rules_information(self):
        if self.previous_board is not None:
            for power in self.previous_board.powers:
                element = self.board.retrieve_element(power)
                if power.type != element.type:
                    if power.type == Element.FIRE_BOMB_POWER and element.is_player():
                        self.rules.increase_bomb_magnitude(element)
                    elif power.type == Element.EXTRA_BOMB_POWER and element.is_player():
                        self.rules.increase_bombs_quantity(element)
                    print "Poder %s fue conseguido por %s " % (power.type, element.type)
        print "Poderes: %s . %s" % (self.rules.players_bomb_magnitude, self.rules.players_bombs_quantity)

    # Calculate bomb ranges
    def calculate_bomb_ranges(self):

        # Iterate each bomb explosion possibility in order to take an action
        for bomb in self.board.bombs:
            # Initialize the directions to go in that direction
            directions = \
                {
                    Action.NORTH: True,
                    Action.SOUTH: True,
                    Action.WEST: True,
                    Action.EAST: True
                }
            possible_players = self.retrieve_possible_put_players(bomb)

            # Evaluates each direction
            for direction in directions:
                magnitude = 1
                injured_element = bomb
                # Only if is possible to advance in that direction (False value means which is not possible advance)
                while directions[direction] and magnitude <= self.rules.retrieve_max_bomb_magnitude(possible_players):
                    # Retrieve the element in the direction of bomb
                    injured_element = self.board.retrieve_element(injured_element, direction)
                    # If cell is not outbound of board
                    if injured_element is not None:
                        # If this bomb are going to impact another bomb, then put most risky bomb type in each one
                        # because two bombs explode at same time (Changed: This affirmation is false for this server)
                        # Remove comments only if this behavior changes
                        # if injured_element.is_bomb():
                            # if bomb.type == Element.TIMER_1_LEFT_BOMB:
                                # injured_element.type = Element.TIMER_1_LEFT_BOMB
                            # if injured_element.type == Element.TIMER_1_LEFT_BOMB:
                                # bomb.type = Element.TIMER_1_LEFT_BOMB
                        # Put the most risky bomb in bomb threat
                        if injured_element.bomb_threat is None:
                            injured_element.bomb_threat = bomb
                        elif injured_element.bomb_threat.type == Element.TIMER_2_LEFT_BOMB:
                            # This is useful for add just the new threat
                            injured_element.reset_individual_effort()
                        # The flame cannot advance over walls
                        if injured_element.is_wall():
                            directions[direction] = False
                        # Increase the cell effort with bomb effort, but decreases a bit in the measure as bot run
                        # away from the bomb in order to avoid the bomb flame if any other way is possible
                        # If injured element is a bomb, then the effort must not be changed
                        if not injured_element.is_bomb():
                            injured_element.increase_effort(bomb.individual_effort - magnitude)

                    magnitude += 1

    # Calculate effort according with distances from bomber killer and elements
    def calculate_effort(self):

        # Effort to move increase 0 in bomber killer place because no movement is necessary
        self.board.bomber_killer.move_effort = self.board.bomber_killer.individual_effort

        # Initial path is established in bomber killer position
        path = [self.board.bomber_killer]

        while len(path) > 0:
            current = path.pop()
            # Obtain contiguous elements to determine its effort
            contiguous_elements = self.board.retrieve_contiguous_elements(current)

            # Determine the effort in each contiguous element
            for contiguous in contiguous_elements:

                if contiguous.is_possible_trace_route():
                    # If is less effort move to contiguous element using this path then set the new effort to that
                    # element and set the current element as its parent
                    if contiguous.move_effort > current.move_effort + contiguous.individual_effort:
                        contiguous.move_effort = current.move_effort + contiguous.individual_effort
                        contiguous.parent = current
                        path.append(contiguous)

            # Delete repeated elements in same path and sort by effort
            path = sorted(frozenset(path), self.move_effort_comparator)

    def calculate_action(self):
        action = None
        objective_reasoning = ""

        # Sort the powers and enemies to obtain the target according with the best path based in their effort
        targets = sorted(self.board.powers + self.board.enemies, self.move_effort_comparator)

        for target in targets:
            next_place = target

            path = [next_place]
            while next_place.parent is not None and next_place.parent != self.board.bomber_killer:
                next_place = next_place.parent
                path.append(next_place)
            path.reverse()

            # If target is unreachable, then try with something else
            if next_place.parent is not None:

                # If is possible move to next element then decide between move or put a bomb on it
                if next_place.is_possible_move_to():
                    action = self.move_or_put_a_bomb(next_place, path)

                    # If movement or bomb are not possible or advance in decided place kill us, then try another target
                    decided_place = self.board.retrieve_element(self.board.bomber_killer, action)
                    if action is not Action.PASS and decided_place.individual_effort <= 40:
                        objective_reasoning += "*Objetivo: %s, Accion: %s*" % (target.type, action)
                        break
                # If an enemy or breakable wall is close to in our path, then try move away
                elif next_place.is_player() or next_place.is_breakable_wall():
                    contiguous_elements = self.board.retrieve_contiguous_elements(self.board.bomber_killer)
                    for contiguous_element in contiguous_elements:
                        if contiguous_element.is_possible_move_to() \
                                and self.predict_safety_after_move(contiguous_element):
                            action = self.move_to(contiguous_element)
                            objective_reasoning += "*Objetivo: %s, Accion: %s (Obstaculo)*" % (target.type, action)
                            break

        # Avoid None action
        if action is None:
            contiguous_elements = self.board.retrieve_contiguous_elements(self.board.bomber_killer)
            for contiguous_element in contiguous_elements:
                if contiguous_element.is_possible_move_to() and self.predict_safety_after_move(contiguous_element):
                    action = self.move_to(contiguous_element)
                    objective_reasoning += "*Objetivo: Ninguno, Accion: %s*" % action

        # Ensure an action
        if action is None:
            action = Action.PASS

        print objective_reasoning

        # If move or stay in decided place kill us, verifying the best option from contiguous elements
        decided_place = self.board.retrieve_element(self.board.bomber_killer, action)
        if decided_place.individual_effort > 40 \
                or (decided_place.individual_effort > 20 and action == Action.PASS):
            print "Riesgo de morir. Vamos a buscar la mejor opcion. "

            possible_places = self.board.retrieve_contiguous_elements(self.board.bomber_killer)
            possible_places.append(self.board.bomber_killer)
            possible_places = sorted(possible_places, self.move_effort_comparator)
            safe_place_found = False
            # Search for the best option to advance (or pass)
            if not safe_place_found:
                more_safe_place = None
                for possible_place in possible_places:
                    if possible_place == self.board.bomber_killer or possible_place.is_possible_move_to():
                        if (more_safe_place is None
                                or more_safe_place.individual_effort > possible_place.individual_effort) \
                                and self.predict_safety_after_move(possible_place):
                            more_safe_place = possible_place
                # If in the more safe place found we don't get be killed, then choose it
                if more_safe_place is not None and more_safe_place.individual_effort <= 40:
                    action = self.move_to(more_safe_place)
                    safe_place_found = True
                    print "Lugar seguro hallado: %s, Accion: %s" % (more_safe_place, action)

            # Search for the best option to advance (or pass)
            if not safe_place_found:
                more_safe_place = None
                for possible_place in possible_places:
                    if possible_place == self.board.bomber_killer or possible_place.is_possible_move_to():
                        if (more_safe_place is None
                                or more_safe_place.individual_effort > possible_place.individual_effort):
                            more_safe_place = possible_place
                # If in the more safe place found we don't get be killed, then choose it
                if more_safe_place is not None and more_safe_place.individual_effort <= 40:
                    action = self.move_to(more_safe_place)
                    safe_place_found = True
                    print "Lugar casi seguro hallado: %s, Accion: %s" % (more_safe_place, action)

            # If no safe place found try to move to a element where a player is with the hope that player will move too
            if not safe_place_found:
                for last_hope_place in possible_places:
                    if last_hope_place.is_player() and last_hope_place != self.board.bomber_killer:
                        action = self.move_to(last_hope_place)
                        safe_place_found = True
                        print "Lugar probable hallado: %s, Accion %s" % (last_hope_place, action)
                        break
            # If no safe place found after this, then we have died :(
            if not safe_place_found:
                print "No hemos encontrado un lugar apropiado :("
        else:
            print "\n"

        self.action = action

    def move_or_put_a_bomb(self, next_place, path):
        # Do not move if will be cover with flames in the next turn or next place flames are very long
        if next_place.individual_effort <= 40 and self.predict_safety_after_move(next_place):
            action = self.move_to(next_place)
        else:
            action = Action.PASS

        # Move to bomb range is dangerous but put a bomb there is even more dangerous (Changed: if a bomb explode over
        # other bomb, not a chain sequence is activated, the other bomb remains normal until it explodes, change if
        # chain reaction is activated in the server)
        # if not next_place.is_bomb_range():
        # Verify the possibility to put a bomb only if is a space and bomber killer is not in immediate bomb range
        if next_place.is_empty_space() and self.board.bomber_killer.individual_effort <= 40 and self.can_put_bomb():

            # Predict if is possible escape after put a bomb
            if self.predict_safety_after_put_a_bomb(next_place):

                # If an enemy is 6 spaces, randomize a 20% for put a bomb
                if len(path) >= 6 and self.random.random() < 0.2 and path[5].is_player():
                    action = self.put_a_bomb_on(next_place)

                # If an enemy is 5 spaces, randomize a 40% for put a bomb
                if len(path) >= 5 and self.random.random() < 0.4 and path[4].is_player():
                    action = self.put_a_bomb_on(next_place)

                # If an enemy is 4 spaces, randomize a 60% for put a bomb
                if len(path) >= 4 and self.random.random() < 0.6 and path[3].is_player():
                    action = self.put_a_bomb_on(next_place)

                # If an enemy is 3 spaces, randomize a 80% for put a bomb
                if len(path) >= 3 and self.random.random() < 0.8 and path[2].is_player():
                    action = self.put_a_bomb_on(next_place)

                # If an enemy or a breakable wall is obstructing our target, put a bomb in front of
                if len(path) >= 2 and self.random.random() < 1.0 \
                        and (path[1].is_player() or path[1].is_breakable_wall()):
                    action = self.put_a_bomb_on(next_place)
        return action

    def move_to(self, next_element):
        if next_element.y == self.board.bomber_killer.y:
            if next_element.x > self.board.bomber_killer.x:
                return Action.EAST
            elif next_element.x < self.board.bomber_killer.x:
                return Action.WEST
        if next_element.x == self.board.bomber_killer.x:
            if next_element.y < self.board.bomber_killer.y:
                return Action.NORTH
            elif next_element.y > self.board.bomber_killer.y:
                return Action.SOUTH
        return Action.PASS

    def put_a_bomb_on(self, next_element):
        if next_element.y == self.board.bomber_killer.y:
            if next_element.x > self.board.bomber_killer.x:
                return Action.BOMB_EAST
            elif next_element.x < self.board.bomber_killer.x:
                return Action.BOMB_WEST
        elif next_element.x == self.board.bomber_killer.x:
            if next_element.y < self.board.bomber_killer.y:
                return Action.BOMB_NORTH
            elif next_element.y > self.board.bomber_killer.y:
                return Action.BOMB_SOUTH
        return Action.PASS

    def retrieve_possible_put_players(self, bomb):
        possible_players = []
        if bomb is not None:
            if bomb.type == Element.TIMER_2_LEFT_BOMB:
                for element in self.board.retrieve_contiguous_elements(bomb):
                    if element.is_alive_player():
                        possible_players.append(element)
            elif bomb.type == Element.TIMER_1_LEFT_BOMB:
                for element in self.previous_board.retrieve_contiguous_elements(bomb):
                    if element.is_alive_player():
                        possible_players.append(element)
        return possible_players

    def can_put_bomb(self):
        put_bombs = 0
        if self.board is not None:
            for bomb in self.board.bombs:
                if bomb.type == Element.TIMER_2_LEFT_BOMB:
                    for element in self.board.retrieve_contiguous_elements(bomb):
                        if element == self.board.bomber_killer:
                            put_bombs += 1
        if self.previous_board is not None:
            for bomb in self.previous_board.bombs:
                if bomb.type == Element.TIMER_2_LEFT_BOMB:
                    for element in self.previous_board.retrieve_contiguous_elements(bomb):
                        if element == self.previous_board.bomber_killer:
                            put_bombs += 1
        if self.old_board is not None:
            for bomb in self.old_board.bombs:
                if bomb.type == Element.TIMER_2_LEFT_BOMB:
                    for element in self.old_board.retrieve_contiguous_elements(bomb):
                        if element == self.old_board.bomber_killer:
                            put_bombs += 1
        return put_bombs < self.rules.retrieve_bombs_quantity(self.board.bomber_killer)

    def predict_safety_after_put_a_bomb(self, bomb_place):
        # Ensure that is possible escape after putting a bomb
        contiguous_elements = self.board.retrieve_contiguous_elements(self.board.bomber_killer)
        for contiguous_element in contiguous_elements:
            if contiguous_element.is_safe_move_to() and contiguous_element != bomb_place:
                future_elements = self.board.retrieve_contiguous_elements(contiguous_element)
                is_safe_to_move = True
                for future_element in future_elements:
                    if future_element.is_alive_player() and future_element != self.board.bomber_killer:
                        is_safe_to_move = False
                if is_safe_to_move:
                    return True
        return False

    def predict_safety_after_move(self, next_place):
        if self.board.bomber_killer.individual_effort > 40:
            future_elements = self.board.retrieve_contiguous_elements(next_place)
            for future_element in future_elements:
                if future_element.is_alive_player() and future_element != self.board.bomber_killer:
                    return False
        return True
