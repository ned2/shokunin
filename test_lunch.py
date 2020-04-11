import itertools

import lunch


def string_to_room(room_str):
    return [[int(cell) for cell in row.split()] for row in room_str.strip().split("\n")]


# test that position gets only valid moves
valid_moves_room = """
0 1 0 0 0 0 0 0 0 1
0 0 1 0 1 1 0 0 0 1
0 0 1 1 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 1 0 1 0 0 1 1
0 1 1 0 1 0 0 0 1 1
0 0 0 0 0 1 1 1 1 1
1 0 0 0 0 1 0 1 0 1
0 1 0 1 0 1 1 0 0 0
0 0 0 0 2 0 1 1 0 0
"""


solvable_room = """
1 0 0 1 0 1 1 0 0 0
0 1 0 0 1 1 0 0 1 1
1 1 1 0 0 0 0 1 1 1
0 0 1 0 0 0 1 1 1 1
0 0 0 1 0 0 1 0 0 1
1 1 1 1 0 0 0 1 0 0
0 0 0 0 0 0 1 0 1 1
0 1 0 0 0 0 1 0 0 0
1 0 0 0 0 1 1 1 1 0
1 0 1 0 0 1 0 0 2 0
"""

def test_room_is_square():
    room = lunch.make_random_room(0.5)
    assert (len(room)) == len(room[0])


def test_room_data_structure():
    room = lunch.make_random_room(0.5)
    assert isinstance(room, list)
    assert isinstance(room[0], list)


def test_room_integers():
    room = lunch.make_random_room(0.5)
    desks = itertools.chain.from_iterable(room)
    assert all([isinstance(desk, int) for desk in desks])


def test_can_move_everywhere():
    room = string_to_room(valid_moves_room)
    moves = lunch.get_valid_moves(room, (7, 2))
    assert (6, 2) in moves
    assert (8, 2) in moves
    assert (7, 1) in moves
    assert (7, 3) in moves


def test_cant_move_anywhere():
    room = string_to_room(valid_moves_room)
    moves = lunch.get_valid_moves(room, (7, 6))
    assert len(moves) == 0


def test_bottom_left_move():
    room = string_to_room(valid_moves_room)
    moves = lunch.get_valid_moves(room, (9, 0))
    assert (9, 1) in moves
    assert (8, 0) in moves


def test_bottom_right_move():
    room = string_to_room(valid_moves_room)
    moves = lunch.get_valid_moves(room, (9, 9))
    assert (9, 8) in moves
    assert (8, 9) in moves

    
def test_can_find_lunch():
    room = string_to_room(solvable_room)
    assert(lunch.can_get_lunch(room, (9, 4)))


def test_cant_find_lunch():
    room = string_to_room(solvable_room)
    assert(not lunch.can_get_lunch(room, (9, 9)))
