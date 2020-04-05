import random


def select_desks(proportion_full, board_size):
    """Returns a set of desks as row,col tuples that have people in them"""
    num_full_desks = int(proportion_full * board_size * board_size)
    filled_desks = set()
    you = board_size-1,random.randrange(board_size)

    while len(filled_desks) <= num_full_desks:
        row = random.randrange(board_size)
        col = random.randrange(board_size)
        desk = row,col
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
    you, filled_desks = select_desks(proportion_full, board_size)
    room = make_room(filled_desks, board_size)
    room[you[0]][you[1]] = 2
    return room


def pretty_print_room(room):
    """Prints the values of a list of lists as a matrix"""
    print("\n".join(" ".join(str(col) for col in row) for row in room))


def can_get_lunch(room):
    """Returns True if given room supports getting lunch, otherwise False"""
    # the exit is any desk in the front row
    # how do I select the start desk?
    pass
