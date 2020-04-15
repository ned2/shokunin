"""Click command line script for accessing luncher solutions"""

import click

from .lunch import (
    get_probabilities,
    estimate_lunch_prob,
    DEFAULT_SAMPLES,
    DEFAULT_INCREMENTS,
    ROOM_SIZE,
)


@click.group()
def main():
    pass


@main.command(name="solve-one")
@click.argument("proportion", type=float)
@click.option("--samples", default=DEFAULT_SAMPLES)
@click.option("--room-size", default=ROOM_SIZE)
def solve_one(proportion, samples, room_size):
    prob = estimate_lunch_prob(proportion, samples)
    click.echo(f"Probability of finding lunch in a {room_size}x{room_size} room: {prob:.3f}")


@main.command(name="solve-all")
@click.option("--samples", default=DEFAULT_SAMPLES)
@click.option("--increments", default=DEFAULT_INCREMENTS)
@click.option("--room-size", default=ROOM_SIZE)
def solve_all(samples, increments, room_size):
    df = get_probabilities(increments, samples)
    top = f"Number of samples for each p: {samples}"
    results = "\n".join(
        f"{x.proportion:.1f} {x.probability:.3f}"
        for x in df.sort_values(by="proportion", ascending=False).itertuples()
    )
    click.echo(f"{top}\n{results}")
