import lunch


def test_room_is_square():
    room = lunch.make_random_room(0.5)
    assert(len(room)) == len(room[0])

    
def test_room_data_structure():
    room = lunch.make_random_room(0.5)
    assert(isinstance(room, list))
    assert(isinstance(room[0], list))

# test that position gets only valid moves
    
# test that solvable room is solvable

# test that unsolvable room is unsolvable


