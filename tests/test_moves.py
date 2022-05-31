import pytest
from cube.cube import *

@pytest.fixture
def cube():
    yield Cube3x3()

@pytest.mark.parametrize("moves_string, expected_edges", [
    ("", "wwwwooooggggrrrrbbbbyyyy"),
    ("R", "wgwwoooogyggrrrrbbbwybyy"),
    ("U", "wwwwgooorgggbrrrobbbyyyy"),
    ("L", "wwwboooogggwrrrrbybbyyyg"),
    ("D", "wwwwooboggogrrgrbbrbyyyy"),
    ("B", "rwwwooowggggryrrbbbbyyoy"),
    ("F", "wwowoyooggggrrrwbbbbryyy"),
] )
def test_move_edges(cube, moves_string, expected_edges):
    c1 = move(cube, moves_string)
    edges = "".join(c1.edges_state)
    assert edges == expected_edges


@pytest.mark.parametrize("moves_string, expected_corners", [
    ("", "wwwwooooggggrrrrbbbbyyyy"),
    ("R", "wggwoooogyygrrrrwbbwybby"),
    ("U", "wwwwggoorrggbbrroobbyyyy"),
    ("L", "bwwboooowggwrrrrbyybgyyg"),
    ("D", "wwwwoobbggoorrggbbrryyyy"),
    ("B", "rrwwwoowggggryyrbbbbyyoo"),
    ("F", "wwoooyyoggggwrrwbbbbrryy"),
] )
def test_move_corners(cube, moves_string, expected_corners):
    c1 = move(cube, moves_string)
    corners = "".join(c1.corners_state)
    assert corners == expected_corners
