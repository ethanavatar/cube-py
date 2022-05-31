from copy import copy
import dataclasses
import typing as t

from .moves import swaps_table

UNICODE_COLORS = {
    'r': u"\u001b[31m",
    'g': u"\u001b[32m",
    'y': u"\u001b[33m",
    'b': u"\u001b[34m",
    'w': u"\u001b[37m",
    'o': u"\u001b[35m"
}

@dataclasses.dataclass
class Cube:
    edges_state: t.AnyStr
    corners_state: t.AnyStr
    edges_orientation: t.List
    corners_orientation: t.List

class Cube3x3(Cube):
    def __init__(self, state : Cube = None):
        if state:
            self.edges_state = copy(state.edges_state)
            self.corners_state = copy(state.corners_state)
            
            self.edges_orientation = copy(state.edges_orientation)
            self.corners_orientation = copy(state.corners_orientation)
            return

        self.edges_state = [c for c in 'wwwwooooggggrrrrbbbbyyyy']
        self.corners_state = [c for c in 'wwwwooooggggrrrrbbbbyyyy']
        
        self.edges_orientation = [0] * 24
        self.corners_orientation = [0] * 24

    def get_edge(self, index):
        return self.edges_state[index], self.edges_orientation[index]

    def get_corner(self, index):
        return self.corners_state[index], self.corners_orientation[index]

    def to_printable(self):
        ch = u"\u25A0\u001b[0m"
        wcuni = UNICODE_COLORS['w']
        ocuni = UNICODE_COLORS['o']
        gcuni = UNICODE_COLORS['g']
        rcuni = UNICODE_COLORS['r']
        bcuni = UNICODE_COLORS['b']
        ycuni = UNICODE_COLORS['y']

        ce = []
        cc = []
        for sticker in self.edges_state:
            ce.append(UNICODE_COLORS[sticker])

        for sticker in self.corners_state:
            cc.append(UNICODE_COLORS[sticker])     

        return f"""
        {cc[0]}{ch} {ce[0]}{ch} {cc[1]}{ch}
        {ce[3]}{ch} {wcuni}{ch} {ce[1]}{ch}
        {cc[3]}{ch} {ce[2]}{ch} {cc[2]}{ch}

{cc[4]}{ch} {ce[4]}{ch} {cc[5]}{ch}\t{cc[8]}{ch} {ce[8]}{ch} {cc[9]}{ch}\t{cc[12]}{ch} {ce[12]}{ch} {cc[13]}{ch}\t{cc[16]}{ch} {ce[16]}{ch} {cc[17]}{ch}
{ce[7]}{ch} {ocuni}{ch} {ce[5]}{ch}\t{ce[11]}{ch} {gcuni}{ch} {ce[9]}{ch}\t{ce[15]}{ch} {rcuni}{ch} {ce[13]}{ch}\t{ce[19]}{ch} {bcuni}{ch} {ce[17]}{ch}
{cc[7]}{ch} {ce[6]}{ch} {cc[6]}{ch}\t{cc[11]}{ch} {ce[10]}{ch} {cc[10]}{ch}\t{cc[15]}{ch} {ce[14]}{ch} {cc[14]}{ch}\t{cc[19]}{ch} {ce[18]}{ch} {cc[18]}{ch}

        {cc[20]}{ch} {ce[20]}{ch} {cc[21]}{ch}
        {ce[23]}{ch} {ycuni}{ch} {ce[21]}{ch}
        {cc[23]}{ch} {ce[22]}{ch} {cc[22]}{ch}
"""

def _swap(state, orientation, a, b):
    state[a], state[b] = state[b], state[a]
    orientation[a], orientation[b] = orientation[b], orientation[a]

def parse_moves(moves_string : t.AnyStr):
    lst = moves_string.split(" ")
    out = []
    for move in lst:
        move = move.upper()

        if len(move) == 1:
            out.append(move)
            continue

        elif move[1] == "'":
            out.extend(move[0] * 3)

        elif int(move[1]):
            out.extend(move[0] * int(move[1]))

    return out


def move(cube : Cube, moves_string : t.AnyStr=""):

    if not moves_string:
        return cube

    new_cube = Cube3x3(cube)

    parsed_moves = parse_moves(moves_string)

    for move in parsed_moves:
        move_name = move[0]
        
        if move not in swaps_table:
            raise NameError(f"move {move} is not valid")

        for peiceType, group in enumerate(swaps_table[move_name]):

            for pair in group:

                # pieceType = 0: corners
                if peiceType == 0:
                    _swap(new_cube.corners_state, new_cube.corners_orientation, pair[0], pair[1])
                
                # pieceType = 1: edges
                elif peiceType == 1:
                    _swap(new_cube.edges_state, new_cube.edges_orientation, pair[0], pair[1])
                
        # R increments the orientation of corners UFR and BRD
        # and decrements the orientation of corners URB and FRD
        if move == 'R':
            for piece in [1, 13, 16, 10, 15, 21]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] + 1 if new_cube.corners_orientation[piece] != 2 else 0
            for piece in [2, 9, 12, 14, 19, 22]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] - 1 if new_cube.corners_orientation[piece] != 0 else 2

        # `U` Doesnt affect any orientation
        
        # L increments the orientation of corners ULB and LFD
        # and decrements the orientation of corners ULF and LBD
        if move == 'L':
            for piece in [3, 5, 8, 7, 18, 23]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] + 1 if new_cube.corners_orientation[piece] != 2 else 0
            for piece in [0, 4, 17, 6, 11, 20]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] - 1 if new_cube.corners_orientation[piece] != 0 else 2

        # `D` Doesnt affect any orientation

        if move == 'F':
            for piece in [2, 5, 8, 9, 10, 11, 15, 20]:
                new_cube.edges_orientation[piece] ^= 1

            for piece in [2, 9, 12, 6, 11, 20]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] + 1 if new_cube.corners_orientation[piece] != 2 else 0
            for piece in [3, 5, 8, 10, 15, 21]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] - 1 if new_cube.corners_orientation[piece] != 0 else 2

        elif move == 'B':
            for piece in [0, 7, 13, 16, 17, 18, 19, 22]:
                new_cube.edges_orientation[piece] ^= 1

            for piece in [0, 4, 17, 14, 19, 22]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] + 1 if new_cube.corners_orientation[piece] != 2 else 0
            for piece in [1, 13, 16, 7, 18, 23]:
                new_cube.corners_orientation[piece] = new_cube.corners_orientation[piece] - 1 if new_cube.corners_orientation[piece] != 0 else 2
    return new_cube


