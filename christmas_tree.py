import argparse
import random


#
# Print your Python Xmas tree :)
#
# python christmas_tree(10)
#
#      *
#     *@*
#    @*@**
#   **@@***
#  *@@***@@*
# @*@@*@*****
#      #
#

class BColors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DARKYELLOW = '\033[33m'
    ENDC = '\033[0m'


def print_christmas_tree(tree_base_size: int) -> None:
    tree_base_size = tree_base_size + 1 if tree_base_size % 2 == 0 else tree_base_size
    steps = 1
    whites = tree_base_size // 2

    print(' ' * whites + f'{BColors.YELLOW}★{BColors.ENDC}')

    while steps <= tree_base_size:
        decoration = [char for char in (f'*' * steps)]
        for i in range(len(decoration) // 2):
            decoration[int(random.random() * len(decoration))] = f'{BColors.RED}@{BColors.ENDC}'

        print(' ' * whites + ''.join(decoration))
        steps = steps + 2
        whites = whites - 1

    print(' ' * (tree_base_size // 2) + f'{BColors.DARKYELLOW}#{BColors.ENDC}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print an ASCII Christmas Tree')
    parser.add_argument("tree_base_size", metavar='N', type=int, help="size of tree base")
    args = parser.parse_args()

    print_christmas_tree(args.tree_base_size)
