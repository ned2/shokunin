from itertools import chain

from lunch import Room


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

solvable_room2 = """
1 0 1 1 1 0 1 0 1 0
1 0 1 1 0 0 1 1 0 1
0 0 0 1 0 0 1 0 0 0
0 1 1 0 0 1 1 0 1 0
0 1 0 0 0 0 0 1 0 0
1 1 0 0 1 0 0 1 0 1
1 0 0 0 0 0 0 1 0 0
1 0 0 1 0 0 1 1 1 1
1 0 0 0 1 0 0 1 0 0
0 0 2 0 0 1 1 1 1 0"""

# TODO: add test for validating the right number of desks
# are assigned for different values of p


def test_room_is_square():
    room = Room(0.5)
    assert len(room.desks) == len(room.desks[0])


def test_room_data_structure():
    room = Room(0.5)
    assert isinstance(room.desks, list)
    assert isinstance(room.desks[0], list)


def test_room_integers():
    room = Room(0.5)
    desks = chain.from_iterable(room.desks)
    assert all([isinstance(desk, int) for desk in desks])


def test_can_move_everywhere():
    room = Room.from_str(valid_moves_room)
    moves = room._get_valid_moves((7, 2))
    assert (6, 2) in moves
    assert (8, 2) in moves
    assert (7, 1) in moves
    assert (7, 3) in moves


def test_cant_move_anywhere():
    room = Room.from_str(valid_moves_room)
    moves = room._get_valid_moves((7, 6))
    assert len(moves) == 0


def test_bottom_left_move():
    room = Room.from_str(valid_moves_room)
    moves = room._get_valid_moves((9, 0))
    assert (9, 1) in moves
    assert (8, 0) in moves


def test_bottom_right_move():
    room = Room.from_str(valid_moves_room)
    moves = room._get_valid_moves((9, 9))
    assert (9, 8) in moves
    assert (8, 9) in moves


def test_can_find_lunch():
    room = Room.from_str(solvable_room)
    assert room._find_lunch_solution((9, 4)) is not None


def test_cant_find_lunch():
    room = Room.from_str(solvable_room)
    assert room._find_lunch_solution((9, 9)) is None

    
def test_serialise_deserialise_room():
    room = Room(0.6)
    room_str = room.to_str()
    new_room = Room.from_str(room_str)
    assert new_room.to_str() == room_str

    
def test_short_solution():
    room = Room.from_str(solvable_room2)
    assert len(room.solution) == 13

