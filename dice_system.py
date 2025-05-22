from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import icepool as ip
from icepool import Die, d


def dieGraph(die: Die) -> None:
    """Graph the probablity of a dice roll"""
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.bar(
        die.keys(), [value / die.denominator() for value in die.values()]
    )  # Plot some data on the Axes.
    ax.set_ylim(0, 1)
    plt.show()


def outcomes(count, num):
    # A single die. Count the number of 6s and 4+s.
    bitd = ip.d(num).map(lambda x: ip.vectorize(x == 6, x >= 4))

    # Interpret the number of dice that rolled the above.
    def count_bitd(outcome):
        sixes, four_pluses = outcome
        if sixes > 1:
            return "3. critical success"
        elif sixes == 1:
            return "2. full success"
        elif four_pluses >= 1:
            return "1. mixed success"
        else:
            return "0. bad outcome"

    # Roll 4 dice and interpret the result.
    print((count @ bitd).map(count_bitd))


def main() -> None:
    die: Die = 2 @ d(8)
    dieGraph(die)
    outcomes(4, 8)


if __name__ == "__main__":
    main()
