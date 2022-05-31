# cube-py

A Rubik's cube data-structure for python.

# Installation

You can install the latest commit using the following command:
```bash
$ pip install git+https://github.com/ethanavatar/cube-py.git
```

## Usage

```python
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
```

**NOTE:** `Cube3x3.to_printable()` uses command line unicode styling for the colors, otherwise its just a bunch of white squares

The above example will print:
![](/static/demo_output.png)