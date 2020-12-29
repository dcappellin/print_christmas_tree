import argparse
import random


def print_christmas_tree(stars: int) -> None:

    stars = stars + 1 if stars % 2 == 0 else stars
    steps = 1
    whites = stars / 2

    while (steps <= stars):
        decorationS = '*' * steps
        decoration = [char for char in decorationS]
        for i in range(int(len(decorationS)/2)):
            position = int(random.random() * len(decorationS))
            decoration[position] = '@'

        print(' ' * int(whites) + ''.join(decoration))
        steps = steps + 2
        whites = whites - 1

    print(' ' * int(stars/2) + '#')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print an ASCII Christmas Tree')

    parser.add_argument("stars", metavar='N', type=int, help="number of stars")

    args = parser.parse_args()

    print_christmas_tree(args.stars)
