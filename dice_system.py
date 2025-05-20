from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import icepool as ip
from icepool import Die, d


def dieGraph(die: Die) -> None:
    """Graph the probablity of one die roll"""
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.bar(
        die.keys(), [value / die.denominator() for value in die.values()]
    )  # Plot some data on the Axes.
    ax.set_ylim(0, 1)
    plt.show()


def main() -> None:
    die: Die = 2 @ d(8)
    dieGraph(die)


if __name__ == "__main__":
    main()
