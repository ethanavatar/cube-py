# TODO: make installable package
from cube import *

# create a new, solved cube
c = Cube3x3()

# create a new cube whose state is a result of applying moves to the solved cube
checkers = move(c, "R2 L2 U2 D2 F2 B2")

# the original cube-state; unchanged
print(c.to_printable())

# checkers
print(checkers.to_printable())