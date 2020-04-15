# Shokunin: Open Space-ial Distancing

`luncher` is a Python package that represents a solution to the Open Space-ial Distancing Shokunin. 

## Installation

To install `luncher`, create a Python 3.6+ virtual environment, `cd` into the cloned repository and run the following:

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

Both commands can take the arguments `--room-size` and `--samples`, which allows solutions to be explored for different sized offices and with different numbers of randomly generated offices, respectively. The `solve-all`command also takes an --increments parameter, allowing you to change the value `p` is incremented by (and thus the number of probabilitues generated).

## Tests

Tests are found in the `tests` directory. Simply run:

    pytest


## Solution

```
Number of samples for each p: 1000000
1.0 0.000
0.9 0.000
0.8 0.000
0.7 0.000
0.6 0.005
0.5 0.068
0.4 0.380
0.3 0.813
0.2 0.968
0.1 0.996
0.0 1.000
```
_Note: that this output was produced by the `solve-all` command described above._

The methodology taken in this solution is to randomly generate populated offices for given `p` values and test whether each generated office permits lunch to be found. The estimated probability is then simply the number of lunch-obtianing offices diovided by the total number of smapled offices. 

The `Room` class within `luncher.py` represents a randomly generated office. See the method `_find_lunch_solution` for the algorthim for testing whether a randomly generated room supports finding lunch. Its docstring contains a detailed description of how the algorithm works.

### Randomly generated room with p=0.4 that supports finding lunch:

```
1 1 1 0 * 1 1 1 1 0
1 1 0 1 * 0 0 0 0 0
0 1 0 * * 1 0 1 0 1
0 0 1 * 0 0 1 0 0 0
1 0 0 * 1 1 0 1 1 0
0 1 1 * 1 1 1 0 0 0
1 * * * 0 1 0 1 0 1
0 * 0 0 1 1 0 1 0 0
1 * 0 0 1 0 0 0 1 1
2 * 1 0 1 0 0 0 0 0
```

### Randomly generated room with p=0.4 that does not supports finding lunch:

```
0 0 0 0 0 1 0 1 1 1
1 0 0 0 1 1 1 1 1 0
1 0 1 1 0 1 1 1 1 1
0 1 1 1 1 1 0 0 0 0
1 0 1 0 1 0 0 0 0 0
0 0 0 0 0 1 0 1 1 0
1 0 0 0 0 0 0 0 0 0
0 1 1 0 0 1 0 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 2 1 0 0 1 1 1 1
```
