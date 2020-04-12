import random

import pandas as pd


def select_desks(proportion_full, board_size):
    """Returns a set of desks as row,col tuples that have people in them"""
    num_full_desks = int(proportion_full * board_size * board_size)
    filled_desks = set()
    you = board_size - 1, random.randrange(board_size)

    while len(filled_desks) <= num_full_desks:
        row = random.randrange(board_size)
        col = random.randrange(board_size)
        desk = row, col
        if desk not in filled_desks:
            filled_desks.add(desk)
    return you, filled_desks


def make_room(filled_desks, board_size):
    """Returns a filled room as a list of lists"""
    board = []
    for row in range(board_size):
        row = [1 if (row, col) in filled_desks else 0 for col in range(board_size)]
        board.append(row)
    return board


def make_random_room(proportion_full, board_size=10):
    """Returns a representation of a room filled randomly with people"""
    start, filled_desks = select_desks(proportion_full, board_size)
    room = make_room(filled_desks, board_size)
    room[start[0]][start[1]] = 2
    return room, start


def pretty_print_room(room):
    """Prints the values of a list of lists as a matrix"""
    print("\n".join(" ".join(str(col) for col in row) for row in room))


def get_valid_moves(room, position):
    """Given a room and current position, return a list of valid moved.

    Note: returns desks in ascending order of getting our protagonist closer to
    lunch.
    """
    board_size = len(room)
    row, col = position
    valid_moves = []

    # move down
    if row < board_size - 1 and not room[row + 1][col]:
        valid_moves.append((row + 1, col))
    # move left
    if col != 0 and not room[row][col - 1]:
        valid_moves.append((row, col - 1))
    # move right
    if col < board_size - 1 and not room[row][col + 1]:
        valid_moves.append((row, col + 1))
    # move up
    if row != 0 and not room[row - 1][col]:
        valid_moves.append((row - 1, col))

    return valid_moves


def can_get_lunch(room, position):
    """Returns True if given room supports getting lunch, otherwise False

    This works by recording the path of our protagonist's route taken so far,
    keeping track of all valid moves available at each desk. If a position with
    no valid moves to a new desk is reached, then the protagonist returns the
    last position that had an un-yet explored desk available to it, and that
    desk becomes the next position.

    This is implemented by maintaining a list of state tuples. Each tuple
    contains the current position in the route and a list of available positions
    from that point. A state tuple takes the form of: (position, valid_moves),
    where `position` is a `row,col` tuple and `valid_moves` is a list of
    positions.

    A new state tuple is appended to the list by removing the next available
    desk that can be moved to (the last valid move in the move list in the
    previous state) and generating the possible moves from there. If there are
    no available moves, then a dead end has been reached and this state must be
    removed by popping it off the list, leaving the next available desk from the
    last choice point as the next position to move to.
    """
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
                return False
            position, valid_moves = route[-1]
        else:
            # try next available move
            position = route[-1][1].pop()
            visited.add(position)
            valid_moves = get_valid_moves(room, position)
            state = position, set(valid_moves) - visited
            route.append(state)
            if position[0] == 0:
                # found the lunch truck!
                return True

            
def estimate_lunch_prob(proportion, samples=10000):
    """Estimate the probability that lunch is found for a value of p"""
    num_lunches = 0
    for _i in range(samples):
        room, start = make_random_room(proportion)
        result = can_get_lunch(room, start)
        if result:
            num_lunches +=1
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
