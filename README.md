# Shokunin: Open Space-ial Distancing

`luncher` is a Python package that represents a solution to the Open Space-ial Distancing Shokunin. 

## Installation

To install `luncher`, create a Python 3.6+ virtual environment and then run the following to install:

    pip install .

## Running

Installing the `luncher` package will install the `luncher` executable into your `PATH`. This command line tool provides two commands you can interact with:

```
Usage: luncher [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  solve-all  Get probability estimates for different increments of `p`.
  solve-one  Estimate probability of finding lunch for a given value of `p`.
```

Both commands can take the arguments `--room-size` and `--samples`, which allows solutions to be explored for different sized offices and 

## Tests

Tests are found in the `tests` directory. Simply run:

    pytest


## Solution

```
Number of samples for each p: 100000
1.0 0.000
0.9 0.000
0.8 0.000
0.7 0.000
0.6 0.005
0.5 0.069
0.4 0.381
0.3 0.813
0.2 0.968
0.1 0.997
0.0 1.000
```
_Note: that this output is produced by the `solve-all` command described above._

The methodology taken in this solution is to randomly generate populated offices for given `p` values and 

