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


def outcomes(count: int, consequences: int) -> Die:
    die = ip.d(8).map(lambda x: ip.vectorize(x == 8, x >= 6, x >= 3))

    # Interpret the number of dice that rolled the above.
    def results(outcome):
        eights, six_pluses, three_pluses = outcome

        if eights > 1:
            return "5.Crit Success"
        elif eights == 1:
            return "4. Success"
        elif six_pluses >= 1:
            return "3. Success at Cost"
        elif three_pluses >= 1:
            return "2. Failure"
        else:
            return "1. Critical Failure"

    # Roll and interpret the result.
    return (count @ die).map(results)


def main() -> None:
    for i in range(1, 5):
        print(i)
        dieGraph(outcomes(i, 0))


if __name__ == "__main__":
    main()
