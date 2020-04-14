"""Click command line script for accessing luncher solutions"""

import click

from .lunch import (
    get_probabilities,
    estimate_lunch_prob,
    DEFAULT_SAMPLES,
    DEFAULT_INCREMENTS,
)


@click.group()
def main():
    pass


@main.command(name="solve-one")
@click.argument("proportion", type=float)
@click.option("--samples", default=DEFAULT_SAMPLES)
def solve_one(proportion, samples):
    prob = estimate_lunch_prob(proportion, samples)
    click.echo(prob)


@main.command(name="solve-all")
@click.option("--samples", default=DEFAULT_SAMPLES)
@click.option("--increments", default=DEFAULT_INCREMENTS)
def solve_all(samples, increments):
    df = get_probabilities(increments, samples)
    click.echo(df)
