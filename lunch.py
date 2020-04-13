import random
from itertools import chain

import pandas as pd


class Room:

    # value that the protagonist gets in the room data structure
    protagonist = 2

    def __init__(self, proportion_full, room_size=10, desks=None, start=None):
        self.proportion_full = proportion_full
        self.room_size = room_size
        self.desks = desks
        self.start = start

        if self.desks is None or self.start is None:
            # create a random desk layout and start position
            self.desks, self.start = self._make_random_room()

        self.find_solution()

    def find_solution(self):
        self.solution = self._find_lunch_solution()
        self.found_lunch = False if self.solution is None else True

    def _make_random_room(self):
        """Returns a representation of a room filled randomly with people"""
        start, filled_desks = self._select_desks()
        room = self._make_room(filled_desks)
        room[start[0]][start[1]] = 2
        return room, start

    def _select_desks(self):
        """Returns a set of desks as row,col tuples that have people in them"""
        num_full_desks = int(self.proportion_full * self.room_size ** 2)
        filled_desks = set()
        start = self.room_size - 1, random.randrange(self.room_size)

        while len(filled_desks) < num_full_desks:
            row = random.randrange(self.room_size)
            col = random.randrange(self.room_size)
            desk = row, col
            if desk not in filled_desks:
                filled_desks.add(desk)
        return start, filled_desks

    def _make_room(self, filled_desks):
        """Returns a filled room as a list of lists"""
        room = []
        for row in range(self.room_size):
            row = [
                1 if (row, col) in filled_desks else 0 for col in range(self.room_size)
            ]
            room.append(row)
        return room

    def _get_valid_moves(self, position):
        """Given a room and current position, return a list of valid moved.

        Note: returns desks in ascending order of getting our protagonist closer to
        lunch.
        """
        row, col = position
        valid_moves = []

        # move down
        if row < self.room_size - 1 and not self.desks[row + 1][col]:
            valid_moves.append((row + 1, col))
        # move left
        if col != 0 and not self.desks[row][col - 1]:
            valid_moves.append((row, col - 1))
        # move right
        if col < self.room_size - 1 and not self.desks[row][col + 1]:
            valid_moves.append((row, col + 1))
        # move up
        if row != 0 and not self.desks[row - 1][col]:
            valid_moves.append((row - 1, col))

        return valid_moves

    def _find_lunch_solution(self, position=None):
        """Returns True if given room supports getting lunch, otherwise False

        This works by recording the path of our protagonist's route taken so far,
        keeping track of all valid moves available at each desk. If a position with
        no valid moves to a new desk is reached, then the protagonist returns the
        last position that had an un-yet explored desk available to it, and that
        desk becomes the next position.

        This is implemented by maintaining a list of state tuples. Each tuple
        contains the current position in the route and a list of available positions
        from that point. A state tuple takes the form of: (position, valid_moves),
        where `position` is a `(row,col)` tuple and `valid_moves` is a list of
        positions.

        A new state tuple is appended to the list by removing the next available
        desk that can be moved to (the last valid move in the move list in the
        previous state) and generating the possible moves from there. If there are
        no available moves, then a dead end has been reached and this state must be
        removed by popping it off the list, leaving the next available desk from the
        last choice point as the next position to move to.
        """
        if position is None:
            position = self.start

        # positions visited in the route
        visited = set()

        # initialise the first position
        route = [("start", [position])]
        while True:
            # trying current position
            if len(route[-1][1]) == 0:
                # current state has no more valid moves; backtrack to last available
                # choice point
                route.pop()
                if len(route) == 0:
                    # ran out of pathways; no lunch today
                    return None
            else:
                # try next available move
                position = route[-1][1].pop()
                visited.add(position)
                valid_moves = self._get_valid_moves(position)
                state = position, [desk for desk in valid_moves if desk not in visited]
                route.append(state)
                if position[0] == 0:
                    # found the lunch truck! return the route taken
                    return [state[0] for state in route[1:]]

    def to_str(self, show_solution=False):
        """Convert a room into a printed string"""
        desks = self.desks
        if show_solution and self.found_lunch:
            # copy the desks data structure first
            desks = [[col for col in row] for row in self.desks]
            for row, col in self.solution[1:]:
                desks[row][col] = "*"
        return "\n".join(" ".join(str(col) for col in row) for row in desks)

    @classmethod
    def from_str(cls, room_str):
        """Create a Room from a saved string representation"""
        desks = [
            [int(cell) for cell in row.split()] for row in room_str.strip().split("\n")
        ]

        for row_index, row in enumerate(desks):
            for col_index, desk in enumerate(row):
                if desk == cls.protagonist:
                    start = row_index, col_index

        room_size = len(desks)
        proportion_full = (
            sum(bool(desk) for desk in chain.from_iterable(desks)) / room_size ** 2
        )
        return cls(proportion_full, room_size=room_size, desks=desks, start=start)

    def __str__(self):
        return self.to_str(show_solution=True)

    def __repr__(self):
        return (
            f"Room(proportion_full={self.proportion_full}, room_size={self.room_size})"
        )


def estimate_lunch_prob(proportion, samples=10000):
    """Estimate the probability that lunch is found for a value of p"""
    num_lunches = 0
    for _i in range(samples):
        room = Room(proportion)
        if room.found_lunch:
            num_lunches += 1
    return num_lunches / samples


def get_probabilities(increment=0.1, samples=10000):
    """Estimate the probabilities for increments of p"""
    results = []
    proportions = []
    proportion = 0

    while proportion <= 1.0:
        result = estimate_lunch_prob(proportion, samples)
        results.append(result)
        proportions.append(proportion)
        proportion += increment
    return pd.DataFrame({"proportion": proportions, "probability": results})
