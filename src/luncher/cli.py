"""Click command line script for accessing luncher solutions"""
import pstats
from functools import partial

import click

from .utils import Timer, Profiler
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


@main.command(name="solve-one", help="Estimate probability of finding lunch for a given value of `p`.")
@click.argument("proportion", type=float)
@click.option("--samples", default=DEFAULT_SAMPLES, help="The number of populated offices to simulate.")
@click.option("--room-size", default=ROOM_SIZE, help="The length in desks of a (square) office.")
@click.option("--time/--no-time", default=False, help="Causes this command to be timed.")
@click.option("--profile/--no-profile", default=False, help="Causes this command to be profiled.")
def solve_one(proportion, samples, room_size, time, profile):
    func = partial(estimate_lunch_prob, proportion, samples)
    if time:
        with Timer() as timer:
            prob = func()
        click.echo(f"Code executed in {timer.ellapsed:.2f} seconds")
    elif profile:
        with Profiler() as profiler:
            prob = func()
        ps = pstats.Stats(profiler).sort_stats("cumulative")
        ps.print_stats()
    else:
        prob = func()        
    click.echo(f"Probability of finding lunch in a {room_size}x{room_size} room: {prob:.3f}")


@main.command(name="solve-all", help="Get probability estimates for different increments of `p`.")
@click.option("--samples", default=DEFAULT_SAMPLES, help="The number of populated offices to simulate.")
@click.option("--increments", default=DEFAULT_INCREMENTS, help="The amount to increment `p` by.")
@click.option("--room-size", default=ROOM_SIZE, help="The length in desks of a (square) office.")
def solve_all(samples, increments, room_size):
    df = get_probabilities(increments, samples)
    top = f"Number of samples for each p: {samples}"
    results = "\n".join(
        f"{x.proportion:.1f} {x.probability:.3f}"
        for x in df.sort_values(by="proportion", ascending=False).itertuples()
    )
    click.echo(f"{top}\n{results}")
