# Shokunin: Open Space-ial Distancing

`luncher` is a Python package that represents a solution to the Open Space-ial Distancing Shokunin. 

## Installation

To install `luncher`, create a Python 3.6+ virtual environment and then run the following to install:

    pip install .

## Running

Installing the `luncher` package will install the `luncher` executable into your `PATH`. This command line tool has two commands you can interact with: `solve-one` for estimating the probability for finding lnunch for a given `p` value and `solve-all` for estimating probabilities for different increments of p between 0 and 1:

```
luncher solve-one 0.3 
```

```
luncher solve-all 
```

Both commands can take the arguments 

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

